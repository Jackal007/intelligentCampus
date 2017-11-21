'''
Created on 2017年11月21日

@author: qfWu
'''

if __name__ == 'main':
    from FeatureCalculaters import *
    import tqdm
    
    claculaters = [library.library_study_time.library_study_time(),
                library.library_week_study_time.library_week_study_time(),
                scholarship.scholarship_amount.scholarship_amount(),
                scholarship.scholarship_rank.scholarship_rank(),
                subsidy.subsidy_amount.subsidy_amount(),
                subsidy.subsidy_rank.subsidy_rank(),
        ]
    
    for claculater in tqdm(claculaters):
        claculater.calculate()
        
    # 关闭数据库
    for claculater in tqdm(claculaters):
       claculater.close()

