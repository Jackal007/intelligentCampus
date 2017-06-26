package NB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *���ݿ����ӹ��߸�����
 */
public class DBCON {
	public static final String DRIVER="com.mysql.jdbc.Driver";
	public static final String URL="jdbc:mysql://localhost:3306/intelligentcampustrain?useUnicode=true&characterEncoding=utf-8&useSSL=false";
	public static final String USER="root";
	public static final String PWD="root";
	private static Connection con=null;
	//private PreparedStatement ps;
	private ResultSet rs;
	private Statement  ps = null;
//	private static Statement conn;
	
	
	/**
	 * @throws ClassNotFoundException 
	 * @return�������ݿ�����
	 */
	public static Connection getCon() {
		try {
			try {
				Class.forName(DRIVER);
			} catch (ClassNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			con=DriverManager.getConnection(URL, USER, PWD);
			//conn = con.createStatement(); 
			//System.out.println("���ӳɹ�");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return con;
	}
	
	/**
	 * �ر���Դ 
	 */
	public void closeAll(){
		if(rs!=null){
			try {
				rs.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		if(ps!=null)
			try {
				ps.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
		if(con!=null)
			try {
				con.close();
			} catch (SQLException e) {
				e.printStackTrace();
			}
	}
	
	/**
	 * @param sql sql��� 
	 * @param pras �����б� 
	 * @throws ClassNotFoundException 
	 * @return��Ӱ�������
	 */
	
	public void update(String sql) {
		int resu=0;
		
		con=getCon();
		try {
			ps=con.createStatement();
			resu=ps.executeUpdate(sql);
		
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			closeAll();
		}
		
	}
	
	
	/**
	 * @param sql sql��� 
	 * @param pras
	 * @return �����
	 * @throws ClassNotFoundException 
	 */
	public ResultSet query(String sql){
		con=getCon();
		try {
			ps=con.createStatement();
			rs=ps.executeQuery(sql);
			
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		return rs;
	}
}
