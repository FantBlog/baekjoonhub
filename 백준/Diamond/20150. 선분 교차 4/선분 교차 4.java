import java.io.*;
import java.util.*;

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
	
	public static boolean cross(Line K, Line Q) {
		Point p1 = K.s, p2 = K.e, p3 = Q.s, p4 = Q.e;
		boolean result = false;
		int a = ccw(p1, p2, p3), b = ccw(p1, p2, p4), c = ccw(p3, p4, p1), d = ccw(p3, p4, p2);
		
		if (a * b == -1 && c * d == -1)
			result = true;

		if (a * b == 0 && c * d == -1)
			result = true;

		if (a * b == -1 && c * d == 0)
			result = true;

		if (a * b == 0 && c * d == 0)
			result = true;
		
		// 모두 한 직선 위에 있을 때
		if (a == 0 && b == 0 && c == 0 && d == 0)
			if (!(Math.max(p3.x, p4.x) < Math.min(p1.x, p2.x) || Math.max(p1.x, p2.x) < Math.min(p3.x, p4.x)))
				if (!(Math.max(p3.y, p4.y) < Math.min(p1.y, p2.y) || Math.max(p1.y, p2.y) < Math.min(p3.y, p4.y)))
					result = true;
				else result = false;
			else result = false;
		
		return result;
	}
	
	public static boolean solution(PriorityQueue<Line> pr) {
		// pr 모든 요소 교차 판단 함수
		int N = pr.size();
		boolean result = false;
		Line[] arr = new Line[N];
		for (int i = 0; i < N; i++) arr[i] = pr.poll();
		
		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				if (cross(arr[i], arr[j])) {
					result = true;
				}
			}
		}
		
//		for (int i = 0; i < N; i++) arr[i] = pr.poll();
		
		return result;
	}
	
	public static class Point{
		public int x, y;
				
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static class Line {
		public Point s, e;
				
		public Line(int x, int y, int a, int b) {
			this.s = new Point(x, y);
			this.e = new Point(a, b);
		}
		
		public int getstart_y() {
			return Math.min(this.s.y, this.e.y);
		}
		
		public int getend_y() {
			return Math.max(this.s.y, this.e.y);
		}
	}

	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		Comparator<Line> wait = new Comparator<Line>(){ // 대기힙용 정렬기준
			@Override // 꺼내는건 끝나는 y 좌표 기준
			public int compare(Line o1, Line o2) {
				// TODO Auto-generated method stub
				if (o1.getstart_y() > o2.getstart_y()) return 1;
				else if (o1.getstart_y() == o2.getstart_y()) return 0;
				else return -1;
			}
		};
		
		Comparator<Line> process = new Comparator<Line>(){ // 처리힙용 정렬기준
			@Override // 꺼내는건 끝나는 y 좌표 기준
			public int compare(Line o1, Line o2) {
				// TODO Auto-generated method stub
				if (o1.getend_y() > o2.getend_y()) return 1;
				else if (o1.getend_y() == o2.getend_y()) return 0;
				else return -1;
			}
		};

		PriorityQueue<Line> wt = new PriorityQueue<Line>(wait); // 대기 힙
		PriorityQueue<Line> pr = new PriorityQueue<Line>(process); // 처리 힙

		// 대기 최소 힙으로 y시작이 작은거 순으로 선분 넣음
		// y 좌표를 높여가면서 대기에서 뽑아서 처리힙에 넣음
		// 현재 y높이보다 처리 최소 힙 peek 가 낮아지면 버림
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		
		for (int i = 0; i < N; i++) { // wt에 담기
			st= new StringTokenizer(br.readLine());
			wt.offer(new Line(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
		}
		
		int now_y;
		int result = 0;
		
		while(!wt.isEmpty() || !pr.isEmpty()) {
			
			if (!wt.isEmpty() && pr.size() <= 1) { // 처리 할 수 없다면
				// 맨위만큼 올라간뒤에
				// 맨위에거 뽑아옴
				now_y = wt.peek().getstart_y();
				
				while (!pr.isEmpty() && pr.peek().getend_y() < now_y)
					pr.poll();
				
				pr.offer(wt.poll());
			}
			else { // if (pr.size() > 1) // 처리가 2개 이상이면 
				// 안의 모든 선분에 대해서 교차 파악
				if (solution(pr)) { // 교차하면
					result = 1;
					break;
				}
				else if(!wt.isEmpty()){ // 새로 넣을 놈이 있을때
					// 모두 안겹치면 새로 들어올 녀석의 start_y 보다 end_y가 낮은 놈들은  제거 ( 미만 )
					// 새로 하나 넣을거 이하 제거
					now_y = wt.peek().getstart_y();
					
					while (!pr.isEmpty() && pr.peek().getend_y() < now_y)
						pr.poll();
					
					pr.offer(wt.poll());
				}
				else { // 새로 넣을 놈이 없다? 교차하지도 않는다? 종료
					break;
				}
			}
		}
		
		System.out.println(result);
	}
}