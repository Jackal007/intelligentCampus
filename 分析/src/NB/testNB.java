package NB;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;

import Dao.StudentDao;
import Impl.StudentImpl;

public class testNB {

	/**
	 * data_length �㷨��˼��
	 */
	public static List<Student> list = new ArrayList<Student>();;
	public static double[][] P_Balance_rank = new double[3][4];
	// double[][] P_Score=new double[3][2];
	public static double[][] P_Cost_amount = new double[3][4];
	// PA,PB..�ֱ��ʾ��ѧ�����A��B,C��D�ȼ���ѧ��ĸ���
	public static double PA_subsidy = 0, PB_subsidy = 0, PC_subsidy = 0, PD_subsidy = 0;
	// public static double[][] P_supermarket_cost_rate=new double[3][4];
	// public static double[][] P_dinnerhall_cost_rate=new double[3][4];
	public static double[][] P_library_time_spand = new double[3][4];
	public static double[][] P_library_time = new double[3][4];
	public static double[][] P_book_borrow = new double[3][4];

	// public static double[][] P_cost_time=new double[3][4];
	// public static double[][] P_Score=new double[3][4];
	public static void main(String[] args) {
		// 1.��ȡ���ݣ�����list������

		StudentDao sd = new StudentImpl();
		list = sd.queryAll(1);
		testData();
		analyse();
	}

	public static int classfiy(String s) {
		if (s.equals("A")) {
			return 1;
		} else if (s.equals("B"))
			return 2;
		else if (s.equals("C"))
			return 3;
		else
			return 4;

	}

	// ѵ������������
	public static void testData() {
		// ѵ������
		int A_subsidy = 0, B_subsidy = 0, C_subsidy = 0, D_subsidy = 0; // ��ʾ���A,B,C,D�ȼ�������
		int[] A_balance_rank = { 0, 0, 0, 0 }, B_balance_rank = { 0, 0, 0, 0 }, C_balance_rank = { 0, 0, 0, 0 };
		int[] A_score = { 0, 0, 0, 0 }, B_score = { 0, 0, 0, 0 }, C_score = { 0, 0, 0, 0 };
		int[] A_cost_amount = { 0, 0, 0, 0 }, B_cost_amount = { 0, 0, 0, 0 }, C_cost_amount = { 0, 0, 0, 0 };
		int[] A_book_borrow = { 0, 0, 0, 0 }, B_book_borrow = { 0, 0, 0, 0 }, C_book_borrow = { 0, 0, 0, 0 };
		int[] A_library_time = { 0, 0, 0, 0 }, B_library_time = { 0, 0, 0, 0 }, C_library_time = { 0, 0, 0, 0 };
		int[] A_library_time_spand = { 0, 0, 0, 0 }, B_library_time_spand = { 0, 0, 0, 0 },
				C_library_time_spand = { 0, 0, 0, 0 };
		int[] A_supermarket_cost_rate = { 0, 0, 0, 0 }, B_supermarket_cost_rate = { 0, 0, 0, 0 },
				C_supermarket_cost_rate = { 0, 0, 0, 0 };
		int[] A_dinnerhall_cost_rate = { 0, 0, 0, 0 }, B_dinnerhall_cost_rate = { 0, 0, 0, 0 },
				C_dinnerhall_cost_rate = { 0, 0, 0, 0 };
		int[] A_cost_time = { 0, 0, 0, 0 }, B_cost_time = { 0, 0, 0, 0 }, C_cost_time = { 0, 0, 0, 0 };
		for (int j = 0; j < list.size(); j++) {
			Student bb = list.get(j);
			// System.out.println(bb.getSubsidy());
			if (classfiy(bb.getSubsidy()) == 1)// δ�����ѧ��
			{
				A_subsidy++;
				if (classfiy(bb.getBalance_rank()) == 1)
					A_balance_rank[0]++;
				if (classfiy(bb.getBalance_rank()) == 2)
					B_balance_rank[0]++;
				if (classfiy(bb.getBalance_rank()) == 3)
					C_balance_rank[0]++;
				/*
				 * if(classfiy(bb.getScore())==1) A_score[0]++;
				 * if(classfiy(bb.getScore())==1) B_score[0]++;
				 * if(classfiy(bb.getScore())==1) C_score[0]++;
				 */
				if (classfiy(bb.getCost_amount()) == 1)
					A_cost_amount[0]++;
				if (classfiy(bb.getCost_amount()) == 2)
					B_cost_amount[0]++;
				if (classfiy(bb.getCost_amount()) == 3)
					C_cost_amount[0]++;

				if (classfiy(bb.getBook_borrow()) == 1)
					A_book_borrow[0]++;
				if (classfiy(bb.getBook_borrow()) == 2)
					B_book_borrow[0]++;
				if (classfiy(bb.getBook_borrow()) == 3)
					C_book_borrow[0]++;

				if (classfiy(bb.getLibrary_times()) == 1)
					A_library_time[0]++;
				if (classfiy(bb.getLibrary_times()) == 2)
					B_library_time[0]++;
				if (classfiy(bb.getLibrary_times()) == 3)
					C_library_time[0]++;

				if (classfiy(bb.getLibrary_time_spand()) == 1)
					A_library_time_spand[0]++;
				if (classfiy(bb.getLibrary_time_spand()) == 2)
					B_library_time_spand[0]++;
				if (classfiy(bb.getLibrary_time_spand()) == 3)
					C_library_time_spand[0]++;
				/*
				 * if(classfiy(bb.getCost_supermarket_rate())==1)
				 * A_supermarket_cost_rate[0]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==2)
				 * B_supermarket_cost_rate[0]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==3)
				 * C_supermarket_cost_rate[0]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==1)
				 * A_dinnerhall_cost_rate[0]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==2)
				 * B_dinnerhall_cost_rate[0]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==3)
				 * C_dinnerhall_cost_rate[0]++;
				 */
				/*
				 * if(classfiy(bb.getCost_times())==1) A_cost_time[0]++;
				 * if(classfiy(bb.getCost_times())==2) B_cost_time[0]++;
				 * if(classfiy(bb.getCost_times())==3) C_cost_time[0]++;
				 */
			} else if (classfiy(bb.getSubsidy()) == 2)// ���1000��ѧ��
			{
				B_subsidy++;
				if (classfiy(bb.getBalance_rank()) == 1)
					A_balance_rank[1]++;
				if (classfiy(bb.getBalance_rank()) == 2)
					B_balance_rank[1]++;
				if (classfiy(bb.getBalance_rank()) == 3)
					C_balance_rank[1]++;
				/*
				 * if(classfiy(bb.getScore())==1) A_score[1]++;
				 * if(classfiy(bb.getScore())==2) B_score[1]++;
				 * if(classfiy(bb.getScore())==3) C_score[1]++;
				 */
				if (classfiy(bb.getCost_amount()) == 1)
					A_cost_amount[1]++;
				if (classfiy(bb.getCost_amount()) == 2)
					B_cost_amount[1]++;
				if (classfiy(bb.getCost_amount()) == 3)
					C_cost_amount[1]++;
				if (classfiy(bb.getBook_borrow()) == 1)
					A_book_borrow[1]++;
				if (classfiy(bb.getBook_borrow()) == 2)
					B_book_borrow[1]++;
				if (classfiy(bb.getBook_borrow()) == 3)
					C_book_borrow[1]++;
				if (classfiy(bb.getLibrary_times()) == 1)
					A_library_time[1]++;
				if (classfiy(bb.getLibrary_times()) == 2)
					B_library_time[1]++;
				if (classfiy(bb.getLibrary_times()) == 3)
					C_library_time[1]++;
				if (classfiy(bb.getLibrary_time_spand()) == 1)
					A_library_time_spand[1]++;
				if (classfiy(bb.getLibrary_time_spand()) == 2)
					B_library_time_spand[1]++;
				if (classfiy(bb.getLibrary_time_spand()) == 3)
					C_library_time_spand[1]++;
				/*
				 * if(classfiy(bb.getCost_supermarket_rate())==1)
				 * A_supermarket_cost_rate[1]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==2)
				 * B_supermarket_cost_rate[1]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==3)
				 * C_supermarket_cost_rate[1]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==1)
				 * A_dinnerhall_cost_rate[1]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==2)
				 * B_dinnerhall_cost_rate[1]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==3)
				 * C_dinnerhall_cost_rate[1]++;
				 * if(classfiy(bb.getCost_times())==1) A_cost_time[1]++;
				 * if(classfiy(bb.getCost_times())==2) B_cost_time[1]++;
				 * if(classfiy(bb.getCost_times())==3) C_cost_time[1]++;
				 */
			} else if (classfiy(bb.getSubsidy()) == 3)// ���1500��ѧ��
			{
				C_subsidy++;
				if (classfiy(bb.getBalance_rank()) == 1)
					A_balance_rank[2]++;
				if (classfiy(bb.getBalance_rank()) == 2)
					B_balance_rank[2]++;
				if (classfiy(bb.getBalance_rank()) == 3)
					C_balance_rank[2]++;
				/*
				 * if(classfiy(bb.getScore())==1) A_score[2]++;
				 * if(classfiy(bb.getScore())==2) B_score[2]++;
				 * if(classfiy(bb.getScore())==3) C_score[2]++;
				 */
				if (classfiy(bb.getCost_amount()) == 1)
					A_cost_amount[2]++;
				if (classfiy(bb.getCost_amount()) == 2)
					B_cost_amount[2]++;
				if (classfiy(bb.getCost_amount()) == 3)
					C_cost_amount[2]++;
				if (classfiy(bb.getBook_borrow()) == 1)
					A_book_borrow[2]++;
				if (classfiy(bb.getBook_borrow()) == 2)
					B_book_borrow[2]++;
				if (classfiy(bb.getBook_borrow()) == 3)
					C_book_borrow[2]++;
				if (classfiy(bb.getLibrary_times()) == 1)
					A_library_time[2]++;
				if (classfiy(bb.getLibrary_times()) == 2)
					B_library_time[2]++;
				if (classfiy(bb.getLibrary_times()) == 3)
					C_library_time[2]++;
				if (classfiy(bb.getLibrary_time_spand()) == 1)
					A_library_time_spand[2]++;
				if (classfiy(bb.getLibrary_time_spand()) == 2)
					B_library_time_spand[2]++;
				if (classfiy(bb.getLibrary_time_spand()) == 3)
					C_library_time_spand[2]++;
				/*
				 * if(classfiy(bb.getCost_supermarket_rate())==1)
				 * A_supermarket_cost_rate[2]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==2)
				 * B_supermarket_cost_rate[2]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==3)
				 * C_supermarket_cost_rate[2]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==1)
				 * A_dinnerhall_cost_rate[2]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==2)
				 * B_dinnerhall_cost_rate[2]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==3)
				 * C_dinnerhall_cost_rate[2]++;
				 * if(classfiy(bb.getCost_times())==1) A_cost_time[2]++;
				 * if(classfiy(bb.getCost_times())==2) B_cost_time[2]++;
				 * if(classfiy(bb.getCost_times())==3) C_cost_time[2]++;
				 */
			} else if (classfiy(bb.getSubsidy()) == 2)// ���2000��ѧ��
			{
				D_subsidy++;
				if (classfiy(bb.getBalance_rank()) == 1)
					A_balance_rank[3]++;
				if (classfiy(bb.getBalance_rank()) == 2)
					B_balance_rank[3]++;
				if (classfiy(bb.getBalance_rank()) == 3)
					C_balance_rank[3]++;
				/*
				 * if(classfiy(bb.getScore())==1) A_score[3]++;
				 * if(classfiy(bb.getScore())==2) B_score[3]++;
				 * if(classfiy(bb.getScore())==3) C_score[3]++;
				 */
				if (classfiy(bb.getCost_amount()) == 1)
					A_cost_amount[3]++;
				if (classfiy(bb.getCost_amount()) == 2)
					B_cost_amount[3]++;
				if (classfiy(bb.getCost_amount()) == 3)
					C_cost_amount[3]++;
				if (classfiy(bb.getBook_borrow()) == 1)
					A_book_borrow[3]++;
				if (classfiy(bb.getBook_borrow()) == 2)
					B_book_borrow[3]++;
				if (classfiy(bb.getBook_borrow()) == 3)
					C_book_borrow[3]++;
				if (classfiy(bb.getLibrary_times()) == 1)
					A_library_time[3]++;
				if (classfiy(bb.getLibrary_times()) == 2)
					B_library_time[3]++;
				if (classfiy(bb.getLibrary_times()) == 3)
					C_library_time[3]++;
				if (classfiy(bb.getLibrary_time_spand()) == 1)
					A_library_time_spand[3]++;
				if (classfiy(bb.getLibrary_time_spand()) == 2)
					B_library_time_spand[3]++;
				if (classfiy(bb.getLibrary_time_spand()) == 3)
					C_library_time_spand[3]++;
				/*
				 * if(classfiy(bb.getCost_supermarket_rate())==1)
				 * A_supermarket_cost_rate[3]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==2)
				 * B_supermarket_cost_rate[3]++;
				 * if(classfiy(bb.getCost_supermarket_rate())==3)
				 * C_supermarket_cost_rate[3]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==1)
				 * A_dinnerhall_cost_rate[3]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==2)
				 * B_dinnerhall_cost_rate[3]++;
				 * if(classfiy(bb.getCost_dinnerhall_rate())==3)
				 * C_dinnerhall_cost_rate[3]++;
				 * if(classfiy(bb.getCost_times())==1) A_cost_time[3]++;
				 * if(classfiy(bb.getCost_times())==2) B_cost_time[3]++;
				 * if(classfiy(bb.getCost_times())==3) C_cost_time[3]++;
				 */
			}
		}
		// ���ʼ��㣬��÷�����

		PA_subsidy = A_subsidy * 1.0 / list.size(); // �޷���ȡ��ѧ��ĸ���
		PB_subsidy = B_subsidy * 1.0 / list.size(); // ��ȡ1000��ѧ��ĸ���
		PC_subsidy = C_subsidy * 1.0 / list.size(); // ��ȡ1500��ѧ��ĸ���
		PD_subsidy = D_subsidy * 1.0 / list.size(); // ��ȡ2000��ѧ��ĸ���
		for (int k = 0; k < 4; ++k) {
			if (k == 0) {
				P_Balance_rank[0][k] = 1.0 * A_balance_rank[k] / (A_subsidy * 1.0) + 0.15;
				// System.out.println(P_Balance_rank[0][k]);
				// P_Score[0][k]=1.0*A_score[k]/A_subsidy+0.05;
				P_Cost_amount[0][k] = 1.0 * A_cost_amount[k] / (A_subsidy * 1.0) + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*A_supermarket_cost_rate[k]/(A_subsidy*1.0);
				// System.out.println(A_supermarket_cost_rate[k]);
				// P_dinnerhall_cost_rate[0][k]=1.0*A_dinnerhall_cost_rate[k]/(A_subsidy*1.0);
				P_library_time_spand[0][k] = 1.0 * A_library_time_spand[k] / (A_subsidy * 1.0) + 0.05;
				P_library_time[0][k] = 1.0 * A_library_time[k] / (A_subsidy * 1.0) + 0.05;
				P_book_borrow[0][k] = 1.0 * A_book_borrow[k] / (A_subsidy * 1.0) + 0.05;
				// P_cost_time[0][k]=1.0*A_cost_time[k]/(A_subsidy*1.0);

				P_Balance_rank[1][k] = 1.0 * B_balance_rank[k] / (A_subsidy * 1.0) + 0.15;
				// P_Score[1][k]=1.0*B_score[k]/A_subsidy+0.05;
				P_Cost_amount[1][k] = 1.0 * B_cost_amount[k] / (A_subsidy * 1.0) + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*B_supermarket_cost_rate[k]/(A_subsidy*1.0);
				// P_dinnerhall_cost_rate[0][k]=1.0*B_dinnerhall_cost_rate[k]/(A_subsidy*1.0);
				P_library_time_spand[1][k] = 1.0 * B_library_time_spand[k] / (A_subsidy * 1.0) + 0.05;
				P_library_time[1][k] = 1.0 * B_library_time[k] / (A_subsidy * 1.0) + 0.05;
				P_book_borrow[1][k] = 1.0 * B_book_borrow[k] / (A_subsidy * 1.0) + 0.05;
				// P_cost_time[0][k]=1.0*B_cost_time[k]/(A_subsidy*1.0);

				P_Balance_rank[2][k] = 1.0 * C_balance_rank[k] / (A_subsidy * 1.0) + 0.15;
				// P_Score[2][k]=1.0*C_score[k]/A_subsidy+0.05;
				P_Cost_amount[2][k] = 1.0 * C_cost_amount[k] / (A_subsidy * 1.0) + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*C_supermarket_cost_rate[k]/(A_subsidy*1.0);
				// P_dinnerhall_cost_rate[0][k]=1.0*C_dinnerhall_cost_rate[k]/(A_subsidy*1.0);
				P_library_time_spand[2][k] = 1.0 * C_library_time_spand[k] / (A_subsidy * 1.0) + 0.05;
				P_library_time[2][k] = 1.0 * C_library_time[k] / (A_subsidy * 1.0) + 0.05;
				P_book_borrow[2][k] = 1.0 * C_book_borrow[k] / (A_subsidy * 1.0) + 0.05;
				// P_cost_time[0][k]=1.0*C_cost_time[k]/(A_subsidy*1.0);
			} else if (k == 1) {
				P_Balance_rank[0][k] = 1.0 * A_balance_rank[k] / B_subsidy + 0.15;
				// P_Score[0][k]=1.0*A_score[k]/B_subsidy+0.05;
				P_Cost_amount[0][k] = 1.0 * A_cost_amount[k] / B_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*A_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*A_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[0][k] = 1.0 * A_library_time_spand[k] / B_subsidy + 0.05;
				P_library_time[0][k] = 1.0 * A_library_time[k] / B_subsidy + 0.05;
				P_book_borrow[0][k] = 1.0 * A_book_borrow[k] / B_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*A_cost_time[k]/B_subsidy;

				P_Balance_rank[1][k] = 1.0 * B_balance_rank[k] / B_subsidy + 0.15;
				// P_Score[1][k]=1.0*B_score[k]/B_subsidy+0.05;
				P_Cost_amount[1][k] = 1.0 * B_cost_amount[k] / B_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*B_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*B_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[1][k] = 1.0 * B_library_time_spand[k] / B_subsidy + 0.05;
				P_library_time[1][k] = 1.0 * B_library_time[k] / B_subsidy + 0.05;
				P_book_borrow[1][k] = 1.0 * B_book_borrow[k] / B_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*B_cost_time[k]/B_subsidy;

				P_Balance_rank[2][k] = 1.0 * C_balance_rank[k] / B_subsidy + 0.15;
				// P_Score[2][k]=1.0*C_score[k]/B_subsidy+0.05;
				P_Cost_amount[2][k] = 1.0 * C_cost_amount[k] / B_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*C_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*C_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[2][k] = 1.0 * C_library_time_spand[k] / B_subsidy + 0.05;
				P_library_time[2][k] = 1.0 * C_library_time[k] / B_subsidy + 0.05;
				P_book_borrow[2][k] = 1.0 * C_book_borrow[k] / B_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*C_cost_time[k]/B_subsidy;
			} else if (k == 2) {
				P_Balance_rank[0][k] = 1.0 * A_balance_rank[k] / C_subsidy + 0.15;
				// P_Score[0][k]=1.0*A_score[k]/C_subsidy+0.05;
				P_Cost_amount[0][k] = 1.0 * A_cost_amount[k] / C_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*A_supermarket_cost_rate[k]/C_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*A_dinnerhall_cost_rate[k]/C_subsidy;
				P_library_time_spand[0][k] = 1.0 * A_library_time_spand[k] / C_subsidy + 0.05;
				P_library_time[0][k] = 1.0 * A_library_time[k] / C_subsidy + 0.05;
				P_book_borrow[0][k] = 1.0 * A_book_borrow[k] / C_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*A_cost_time[k]/B_subsidy;

				P_Balance_rank[1][k] = 1.0 * B_balance_rank[k] / C_subsidy + 0.15;
				// P_Score[1][k]=1.0*B_score[k]/C_subsidy+0.05;
				P_Cost_amount[1][k] = 1.0 * B_cost_amount[k] / C_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*B_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*B_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[1][k] = 1.0 * B_library_time_spand[k] / C_subsidy + 0.05;
				P_library_time[1][k] = 1.0 * B_library_time[k] / C_subsidy + 0.05;
				P_book_borrow[1][k] = 1.0 * B_book_borrow[k] / C_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*B_cost_time[k]/C_subsidy;

				P_Balance_rank[2][k] = 1.0 * C_balance_rank[k] / C_subsidy + 0.15;
				// P_Score[2][k]=1.0*C_score[k]/C_subsidy+0.05;
				P_Cost_amount[2][k] = 1.0 * C_cost_amount[k] / C_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*C_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*C_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[2][k] = 1.0 * C_library_time_spand[k] / C_subsidy + 0.05;
				P_library_time[2][k] = 1.0 * C_library_time[k] / C_subsidy + 0.05;
				P_book_borrow[2][k] = 1.0 * C_book_borrow[k] / C_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*C_cost_time[k]/B_subsidy;
			} else {
				P_Balance_rank[0][k] = 1.0 * A_balance_rank[k] / D_subsidy + 0.15;
				// P_Score[0][k]=1.0*A_score[k]/D_subsidy+0.05;
				P_Cost_amount[0][k] = 1.0 * A_cost_amount[k] / D_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*A_supermarket_cost_rate[k]/C_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*A_dinnerhall_cost_rate[k]/C_subsidy;
				P_library_time_spand[0][k] = 1.0 * A_library_time_spand[k] / D_subsidy + 0.05;
				P_library_time[0][k] = 1.0 * A_library_time[k] / D_subsidy + 0.05;
				P_book_borrow[0][k] = 1.0 * A_book_borrow[k] / D_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*A_cost_time[k]/B_subsidy;

				P_Balance_rank[1][k] = 1.0 * B_balance_rank[k] / D_subsidy + 0.15;
				// P_Score[1][k]=1.0*B_score[k]/D_subsidy+0.05;
				P_Cost_amount[1][k] = 1.0 * B_cost_amount[k] / D_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*B_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*B_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[1][k] = 1.0 * B_library_time_spand[k] / D_subsidy + 0.05;
				P_library_time[1][k] = 1.0 * B_library_time[k] / D_subsidy + 0.05;
				P_book_borrow[1][k] = 1.0 * B_book_borrow[k] / D_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*B_cost_time[k]/C_subsidy;

				P_Balance_rank[2][k] = 1.0 * C_balance_rank[k] / D_subsidy + 0.15;
				// P_Score[2][k]=1.0*C_score[k]/D_subsidy+0.05;
				P_Cost_amount[2][k] = 1.0 * C_cost_amount[k] / D_subsidy + 0.05;
				// P_supermarket_cost_rate[0][k]=1.0*C_supermarket_cost_rate[k]/B_subsidy;
				// P_dinnerhall_cost_rate[0][k]=1.0*C_dinnerhall_cost_rate[k]/B_subsidy;
				P_library_time_spand[2][k] = 1.0 * C_library_time_spand[k] / D_subsidy + 0.05;
				P_library_time[2][k] = 1.0 * C_library_time[k] / D_subsidy + 0.05;
				P_book_borrow[2][k] = 1.0 * C_book_borrow[k] / D_subsidy + 0.05;
				// P_cost_time[0][k]=1.0*C_cost_time[k]/B_subsidy;
			}
		}

		/*
		 * for(int i=0;i<3;++i) for(int j=0;j<2;++j) {
		 * System.out.println(P_Balance_rank[i][j]);
		 * System.out.println(P_Score[i][j]);
		 * System.out.println(P_Cost_amount[i][j]);
		 * System.out.println(P_library_time_spand[i][j]);
		 * System.out.println(P_library_time[i][j]);
		 * System.out.println(P_book_borrow[i][j]);
		 * 
		 * }
		 */
	}

	// }
	//
	// ��������
	public static void Analyse_test(String id, String a, String b, String c, String d, String e, String f) {
		double P_Asubsidy = 1.0, P_Bsubsidy = 1.0, P_Csubsidy = 1.0, P_Dsubsidy = 1.0;
		if (a.equals("A")) {
			P_Asubsidy *= P_Balance_rank[0][0];
			P_Bsubsidy *= P_Balance_rank[0][1];
			P_Csubsidy *= P_Balance_rank[0][2];
			P_Dsubsidy *= P_Balance_rank[0][3];
		} else if (a.equals("B")) {
			P_Asubsidy *= P_Balance_rank[1][0];
			P_Bsubsidy *= P_Balance_rank[1][1];
			P_Csubsidy *= P_Balance_rank[1][2];
			P_Dsubsidy *= P_Balance_rank[1][3];
		} else if (a.equals("C")) {
			P_Asubsidy *= P_Balance_rank[2][0];
			P_Bsubsidy *= P_Balance_rank[2][1];
			P_Csubsidy *= P_Balance_rank[2][2];
			P_Dsubsidy *= P_Balance_rank[2][3];
		}

		if (b.equals("A")) {
			P_Asubsidy *= P_book_borrow[0][0];
			P_Bsubsidy *= P_book_borrow[0][1];
			P_Csubsidy *= P_book_borrow[0][2];
			P_Dsubsidy *= P_book_borrow[0][3];
		} else if (b.equals("B")) {
			P_Asubsidy *= P_book_borrow[1][0];
			P_Bsubsidy *= P_book_borrow[1][1];
			P_Csubsidy *= P_book_borrow[1][2];
			P_Dsubsidy *= P_book_borrow[1][3];
		} else if (b.equals("C")) {
			P_Asubsidy *= P_book_borrow[2][0];
			P_Bsubsidy *= P_book_borrow[2][1];
			P_Csubsidy *= P_book_borrow[2][2];
			P_Dsubsidy *= P_book_borrow[2][3];
		}

		if (c.equals("A")) {
			P_Asubsidy *= P_Cost_amount[0][0];
			P_Bsubsidy *= P_Cost_amount[0][1];
			P_Csubsidy *= P_Cost_amount[0][2];
			P_Dsubsidy *= P_Cost_amount[0][3];
		} else if (c.equals("B")) {
			P_Asubsidy *= P_Cost_amount[1][0];
			P_Bsubsidy *= P_Cost_amount[1][1];
			P_Csubsidy *= P_Cost_amount[1][2];
			P_Dsubsidy *= P_Cost_amount[1][3];
		} else if (c.equals("C")) {
			P_Asubsidy *= P_Cost_amount[2][0];
			P_Bsubsidy *= P_Cost_amount[2][1];
			P_Csubsidy *= P_Cost_amount[2][2];
			P_Dsubsidy *= P_Cost_amount[2][3];
		}

		if (d.equals("A")) {
			P_Asubsidy *= P_library_time_spand[0][0];
			P_Bsubsidy *= P_library_time_spand[0][1];
			P_Csubsidy *= P_library_time_spand[0][2];
			P_Dsubsidy *= P_library_time_spand[0][3];
		} else if (d.equals("B")) {
			P_Asubsidy *= P_library_time_spand[1][0];
			P_Bsubsidy *= P_library_time_spand[1][1];
			P_Csubsidy *= P_library_time_spand[1][2];
			P_Dsubsidy *= P_library_time_spand[1][3];
		} else if (d.equals("C")) {
			P_Asubsidy *= P_library_time_spand[2][0];
			P_Bsubsidy *= P_library_time_spand[2][1];
			P_Csubsidy *= P_library_time_spand[2][2];
			P_Dsubsidy *= P_library_time_spand[2][3];
		}

		if (e.equals("A")) {
			P_Asubsidy *= P_library_time[0][0];
			P_Bsubsidy *= P_library_time[0][1];
			P_Csubsidy *= P_library_time[0][2];
			P_Dsubsidy *= P_library_time[0][3];
		} else if (e.equals("B")) {
			P_Asubsidy *= P_library_time[1][0];
			P_Bsubsidy *= P_library_time[1][1];
			P_Csubsidy *= P_library_time[1][2];
			P_Dsubsidy *= P_library_time[1][3];
		} else if (e.equals("C")) {
			P_Asubsidy *= P_library_time[2][0];
			P_Bsubsidy *= P_library_time[2][1];
			P_Csubsidy *= P_library_time[2][2];
			P_Dsubsidy *= P_library_time[2][3];
		}
		/*
		 * if(f.equals("A")) { P_Asubsidy*=P_Score[0][0];
		 * P_Bsubsidy*=P_Score[0][1]; P_Csubsidy*=P_Score[0][2];
		 * P_Dsubsidy*=P_Score[0][3]; } else if(f.equals("B")) {
		 * P_Asubsidy*=P_Score[1][0]; P_Bsubsidy*=P_Score[1][1];
		 * P_Csubsidy*=P_Score[1][2]; P_Dsubsidy*=P_Score[1][3]; } else
		 * if(f.equals("C")) { P_Asubsidy*=P_Score[2][0];
		 * P_Bsubsidy*=P_Score[2][1]; P_Csubsidy*=P_Score[2][2];
		 * P_Dsubsidy*=P_Score[2][3]; }
		 */
		double max = 0.0;
		int tag = 0;
		if (P_Asubsidy > max) {
			tag = 1;
			max = P_Asubsidy;
		}
		if (P_Bsubsidy > max) {
			tag = 2;
			max = P_Bsubsidy;
		}
		if (P_Csubsidy > max) {
			tag = 3;
			max = P_Csubsidy;
		}
		if (P_Dsubsidy > max)
			tag = 4;
		if (tag == 1) {
			// System.out.println("ѧ��Ϊ "+id+" �޷������ѧ��Ŀ����Խϴ�");
			System.out.println(id + ",0");
			method1(id + ",0");
		} else if (tag == 2) {
			// System.out.println("ѧ��Ϊ "+id+" ���1000Ԫ��ѧ��Ŀ����Խϴ�");
			System.out.println(id + ",1000");
			method1(id + ",1000");
		} else if (tag == 3) {
			// System.out.println("ѧ��Ϊ "+id+" ���1500Ԫ��ѧ��Ŀ����Խϴ�");
			System.out.println(id + ",1500");
			method1(id + ",1500");
		} else {
			// System.out.println("ѧ��Ϊ "+id+" ���2000Ԫ��ѧ��Ŀ����Խϴ�");
			System.out.println(id + ",2000");
			method1(id + ",2000");
		}
		P_Asubsidy = 1.0;
		P_Bsubsidy = 1.0;
		P_Csubsidy = 1.0;
		P_Dsubsidy = 1.0;
	}

	public static void analyse() {
		List<Student> test = new ArrayList<Student>();
		StudentDao sd = new StudentImpl();
		test = sd.queryAll(2);
		// Analyse_test("1","A","A","A","B","B","B");
		for (int i = 0; i < test.size(); ++i) {
			Student stu = test.get(i);

			Analyse_test(stu.getStudent_id(), stu.getBalance_rank(), stu.getBook_borrow(), stu.getScore(),
					stu.getCost_amount(), stu.getLibrary_time_spand(), stu.getLibrary_times());
			// Analyse(stu.getStudent_id(),stu.getBalance_rank(),stu.getBook_borrow(),stu.getCost_amount(),stu.getCost_dinnerhall_rate(),stu.getCost_supermarket_rate(),stu.getCost_times(),stu.getLibrary_time_spand(),stu.getLibrary_times());
		}
	}

	public static void method1(String str) {
		FileWriter fw = null;
		try {
			// ����ļ����ڣ���׷�����ݣ�����ļ������ڣ��򴴽��ļ�
			File f = new File("results.txt");
			fw = new FileWriter(f, true);
		} catch (IOException e) {
			e.printStackTrace();
		}
		PrintWriter pw = new PrintWriter(fw);
		pw.println(str);
		pw.flush();
		try {
			fw.flush();
			pw.close();
			fw.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
