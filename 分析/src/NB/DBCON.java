package NB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *锟斤拷锟捷匡拷锟斤拷锟接癸拷锟竭革拷锟斤拷锟斤拷
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
	 * @return锟斤拷锟斤拷锟斤拷锟捷匡拷锟斤拷锟斤拷
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
			//System.out.println("锟斤拷锟接成癸拷");
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return con;
	}
	
	/**
	 * 锟截憋拷锟斤拷源 
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
	 * @param sql sql锟斤拷锟� 
	 * @param pras 锟斤拷锟斤拷锟叫憋拷 
	 * @throws ClassNotFoundException 
	 * @return锟斤拷影锟斤拷锟斤拷锟斤拷锟�
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
	 * @param sql sql锟斤拷锟� 
	 * @param pras
	 * @return 锟斤拷锟斤拷锟�
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
