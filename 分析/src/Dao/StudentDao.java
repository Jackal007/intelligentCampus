package Dao;

import java.util.List;

import NB.Student;


public interface StudentDao {
	public List<Student> queryAll(int tag);
}
