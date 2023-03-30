import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Scanner;

class Main
{	
	public static int ccw(Point a, Point b, Point c) {
		int result;
		
		double x1 = b.x - a.x;
		double x2 = c.x - a.x;
		double y1 = b.y - a.y;
		double y2 = c.y - a.y;
		double top = x1 * y2 - y1 * x2;
		double bottom = Math.sqrt(x1 * x1 + y1 * y1) * Math.sqrt(x2 * x2 + y2 * y2);
		
		double theta = Math.asin(top / bottom);
		
		if (theta > 0) result = 1;
		else if (theta < 0) result = -1;
		else result = 0;
		
		return result;
	}
	
	public static class Point{
		public int x, y;
				
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Point p1, p2, p3, p4;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		p1 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		p2 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		
		st = new StringTokenizer(br.readLine());
		p3 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		p4 = new Point(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		
		int result = 0;
		
		if (ccw(p1, p2, p3) * ccw(p1, p2, p4) == -1 && ccw(p3, p4, p1) * ccw(p3, p4, p2) == -1)
			result = 1;

		if (ccw(p1, p2, p3) * ccw(p1, p2, p4) == 0 && ccw(p3, p4, p1) * ccw(p3, p4, p2) == -1)
			result = 1;

		if (ccw(p1, p2, p3) * ccw(p1, p2, p4) == -1 && ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0)
			result = 1;

		if (ccw(p1, p2, p3) * ccw(p1, p2, p4) == 0 && ccw(p3, p4, p1) * ccw(p3, p4, p2) == 0)
			result = 1;
		
		// 모두 한 직선 위에 있을 때
		if (ccw(p1, p2, p3) == 0 && ccw(p1, p2, p4) == 0 && ccw(p3, p4, p1) == 0 && ccw(p3, p4, p2) == 0)
			if (!(Math.max(p3.x, p4.x) < Math.min(p1.x, p2.x) || Math.max(p1.x, p2.x) < Math.min(p3.x, p4.x)))
				if (!(Math.max(p3.y, p4.y) < Math.min(p1.y, p2.y) || Math.max(p1.y, p2.y) < Math.min(p3.y, p4.y)))
					result = 1;
				else result = 0;
			else result = 0;
		System.out.println(result);
	}
}