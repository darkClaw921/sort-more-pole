# import redisWork
from flask import Flask, request, render_template
from flask_restx import Api, Resource, fields
from pprint import pprint  
from datetime import datetime, timedelta
from workBitrix import get_task_work_time, create_item, \
    get_act_item, sort_billings, update_act_for_item,ACTitem, \
    sort_rashody 
    

app = Flask(__name__)
api = Api(app, version='1.0', title='pkGroup API',description='A pkGroup API sort billing',)

ACT_ITEM_ID=182
BILLING_ENTY_ID=149
RASHODY_ENTY_ID=160 #расходы

@api.route('/sort/<string:entitiID>/<int:itemID>/<string:pole>')
class report_entity(Resource):
    def post(self,entitiID:int,itemID:int, pole:str):
        """Обновление сущности"""
        # pprint(request)
        # userID=userID.split('_')[1] 
        entitiID=entitiID.split('_')[0]
        if entitiID != 'T91': return 'Not report'
        
        # if entitiID == 'T91':
        #     entitiID=ACT_ITEM_ID

        # if entitiID == 'T92':
        #     entitiID=BILLING_ENTY_ID

        # if entitiID == 'T93':
        #     entitiID=RASHODY_ENTY_ID
            
        print(f"{entitiID=}")
        
        print(f"{itemID=}")
        # print(f"{userID=}")

        act=get_act_item(itemID)
        if pole=='billings':
            sort=sort_billings(act[ACTitem.billings])
    
        if pole=='rashody':
            sort=sort_rashody(act[ACTitem.rashody])

        # sort=sort_billings(act[ACTitem.billings])
        pprint(sort)
        # sort.append('111')
        update_act_for_item(itemID, sort, pole)
        

        return 'OK'
    
    # def post(self,):
    #     """Обновление сущности"""
    #     data = request.get_json() 
    #     pprint(data)
    #     # tasks=get_crm_task(13)
    #     # p=prepare_crm_task(tasks)
        
    #     return 'OK'



if __name__ == '__main__':
    
    app.run(host='0.0.0.0',port='5003',debug=True)
    
