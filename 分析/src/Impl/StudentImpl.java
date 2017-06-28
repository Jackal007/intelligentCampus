package Impl;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import Dao.StudentDao;
import NB.DBCON;
import NB.Student;

public class StudentImpl implements StudentDao{
	DBCON util=new DBCON();
	@Override
	public List<Student> queryAll(int tag) {
		if(tag==1)//��ѯǰһ������
			return  _list(util.query("select *  from students order by student_id" ));
		else
			return  _list(util.query("select *  from students order by student_id desc" ));
	}
	private List<Student> _list(ResultSet rs){
		List<Student> _list=new ArrayList<Student>();
		try {
			while(rs.next()){
				Student stu=new Student();
				stu.setScore(rs.getString("score"));
				stu.setStudent_id(rs.getString("student_id"));
				stu.setBalance_rank(rs.getString("balance_rank"));
				stu.setCost_amount(rs.getString("cost_amount"));
				stu.setCost_times(rs.getString("cost_times"));
				stu.setCost_dinnerhall_rate(rs.getString("cost_dinnerhall_rate"));
				stu.setLibrary_times(rs.getString("library_times"));
				stu.setLibrary_time_spand(rs.getString("library_time_spand"));
				stu.setCost_supermarket_rate(rs.getString("cost_supermarket_rate"));
				stu.setCost_avg_dinnerHall(rs.getString("cost_avg_dinnerHall"));
				stu.setSubsidy(rs.getString("subsidy"));
				stu.setCost_supermarket_rate(rs.getString("cost_supermarket_rate"));
				stu.setBook_borrow(rs.getString("library_borrow"));
				_list.add(stu);
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			util.closeAll();
		}
		return _list;
	}
}
