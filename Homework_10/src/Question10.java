import java.util.*;

public class Question10 {

    protected static int[] grid = new int[9];

    protected static int number_of_dirt;

    protected static int vacuum_current_position;

    protected static int type_of_agent;

    protected static int number_of_cleaned_dirt = 0;

    protected static int number_of_steps_to_clean = 0;

    static int score = 0;

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Select any one of the following agent (1, 2, 3, 4): ");
        System.out.println("1. Simple reflex agent ");
        System.out.println("2. Randomized agent");
        System.out.println("3. Simple reflex agent with murphy's law ");
        System.out.println("4. Randomized agent with murphy's law ");
        type_of_agent = scanner.nextInt();

        System.out.println("Enter number of dirt (1, 3, 5) on the grid : ");
        number_of_dirt = scanner.nextInt();

        vacuum_current_position = get_random_in_range(9);

        randomize_dirt_position();

        print_current_situation();

        if (type_of_agent == 1) {

            for (int i = 0; i < 200; i++) {
                if (number_of_cleaned_dirt != number_of_dirt) {
                    work_agent_1();
                    print_current_situation();
                } else {
                    break;
                }
            }
            System.out.println("The agent has took " + number_of_steps_to_clean + " steps. " + "The score is " + (score+number_of_steps_to_clean));

        } else if (type_of_agent == 2) {

            for (int i = 0; i < 200; i++) {
                if (number_of_cleaned_dirt != number_of_dirt) {
                    work_agent_2();
                    print_current_situation();
                } else {
                    break;
                }
            }
            System.out.println("The agent has took " + number_of_steps_to_clean + " steps. " + "The score is " + (score+number_of_steps_to_clean));

        } else if (type_of_agent == 3) {

            for (int i = 0; i < 200; i++) {
                if (number_of_cleaned_dirt != number_of_dirt) {
                    work_agent_3();
                    print_current_situation();
                } else {
                    break;
                }
            }
            System.out.println("The agent has took " + number_of_steps_to_clean + " steps. " + "The score is " + (score+number_of_steps_to_clean));

        } else if (type_of_agent == 4) {

            for (int i = 0; i < 200; i++) {
                if (number_of_cleaned_dirt != number_of_dirt) {
                    work_agent_4();
                    print_current_situation();
                } else {
                    break;
                }
            }
            System.out.println("The agent has took " + number_of_steps_to_clean + " steps. " + "The score is " + (score+number_of_steps_to_clean));

        }
    }

    protected static int get_random_in_range(int high) {
        Random random = new Random();
        int low = 0;
        return random.nextInt(high - low) + low;
    }

    protected static void randomize_dirt_position() {

        List<Integer> list = new ArrayList<Integer>(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8));
        Collections.shuffle(list);

        for (int i = 0; i < grid.length; i++) {
            grid[i] = 0;
        }

        for (int i = 0; i < number_of_dirt; i++) {
            grid[list.get(i)] = 1;
        }
    }

    protected static void print_current_situation() {

        for (int i = 0; i < grid.length; i++) {

            if (vacuum_current_position == i) {
                System.out.print("| v ");
            } else {
                System.out.print("|   ");
            }

            if (grid[i] == 1) {
                System.out.print("d |");
            } else {
                System.out.print("  |");
            }

            if (i == 2 || i == 5 || i == 8) {
                System.out.print("\n");
            }
        }

        System.out.print("\n");
    }

    protected static void work_agent_1() {

        if (grid[vacuum_current_position] == 1) {
            System.out.println("cleaning");
            grid[vacuum_current_position] = 0;
            number_of_cleaned_dirt++;
            score = score + 10;
        } else {

            number_of_steps_to_clean++;

            if (vacuum_current_position == 0) {
                System.out.println("going right");
                vacuum_current_position = 1;
            } else if (vacuum_current_position == 1) {

                vacuum_current_position = 2;

//                if (get_random_in_range(2) == 1) {
//                    System.out.println("going right randomly");
//                    vacuum_current_position = 2;
//                } else {
//                    System.out.println("going left randomly");
//                    vacuum_current_position = 0;
//                }

            } else if (vacuum_current_position == 2) {
                System.out.println("going down");
                vacuum_current_position = 5;
            } else if (vacuum_current_position == 3) {
                System.out.println("going right");
                vacuum_current_position = 4;
            } else if (vacuum_current_position == 4) {
                System.out.println("going up");
                vacuum_current_position = 1;
            } else if (vacuum_current_position == 5) {
                System.out.println("going down");
                vacuum_current_position = 8;
            } else if (vacuum_current_position == 6) {
                System.out.println("going up");
                vacuum_current_position = 3;
            } else if (vacuum_current_position == 7) {
                System.out.println("going left");
                vacuum_current_position = 6;
            } else if (vacuum_current_position == 8) {
                System.out.println("going left");
                vacuum_current_position = 7;
            }

        }
    }

    protected static void work_agent_2() {

        if (grid[vacuum_current_position] == 1) {
            if (get_random_in_range(2) == 1) {
                System.out.println("cleaning");
                grid[vacuum_current_position] = 0;
                number_of_cleaned_dirt++;
                score = score + 10;
            } else {
                System.out.println("not cleaning and moving on");
                move_agent_2_4();
            }

        } else {

            move_agent_2_4();

        }
    }

    protected static void move_agent_2_4() {

        number_of_steps_to_clean++;

        int dir;

        if (vacuum_current_position == 0) {

            dir = get_random_in_range(2);
            if (dir == 0) {
                System.out.println("going right");
                vacuum_current_position = 1;
            } else {
                System.out.println("going down");
                vacuum_current_position = 3;
            }

        } else if (vacuum_current_position == 1) {

            dir = get_random_in_range(3);
            if (dir == 0) {
                System.out.println("going left");
                vacuum_current_position = 0;
            } else if (dir == 1) {
                System.out.println("going down");
                vacuum_current_position = 4;
            } else {
                System.out.println("going right");
                vacuum_current_position = 2;
            }

        } else if (vacuum_current_position == 2) {

            dir = get_random_in_range(2);
            if (dir == 0) {
                System.out.println("going left");
                vacuum_current_position = 1;
            } else {
                System.out.println("going down");
                vacuum_current_position = 5;
            }

        } else if (vacuum_current_position == 3) {

            dir = get_random_in_range(3);
            if (dir == 0) {
                System.out.println("going up");
                vacuum_current_position = 0;
            } else if (dir == 1) {
                System.out.println("going right");
                vacuum_current_position = 4;
            } else {
                System.out.println("going down");
                vacuum_current_position = 6;
            }

        } else if (vacuum_current_position == 4) {

            dir = get_random_in_range(4);
            if (dir == 0) {
                System.out.println("going up");
                vacuum_current_position = 1;
            } else if (dir == 1) {
                System.out.println("going right");
                vacuum_current_position = 5;
            } else if (dir == 2) {
                System.out.println("going down");
                vacuum_current_position = 7;
            } else {
                System.out.println("going left");
                vacuum_current_position = 3;
            }

        } else if (vacuum_current_position == 5) {

            dir = get_random_in_range(3);
            if (dir == 0) {
                System.out.println("going up");
                vacuum_current_position = 2;
            } else if (dir == 1) {
                System.out.println("going left");
                vacuum_current_position = 4;
            } else {
                System.out.println("going down");
                vacuum_current_position = 8;
            }

        } else if (vacuum_current_position == 6) {

            dir = get_random_in_range(2);
            if (dir == 0) {
                System.out.println("going up");
                vacuum_current_position = 3;
            } else {
                System.out.println("going right");
                vacuum_current_position = 7;
            }

        } else if (vacuum_current_position == 7) {

            dir = get_random_in_range(3);
            if (dir == 0) {
                System.out.println("going left");
                vacuum_current_position = 6;
            } else if (dir == 1) {
                System.out.println("going up");
                vacuum_current_position = 4;
            } else {
                System.out.println("going right");
                vacuum_current_position = 8;
            }


        } else if (vacuum_current_position == 8) {

            dir = get_random_in_range(2);
            if (dir == 0) {
                System.out.println("going up");
                vacuum_current_position = 5;
            } else {
                System.out.println("going left");
                vacuum_current_position = 7;
            }

        }
    }

    protected static void work_agent_3() {

        if (grid[vacuum_current_position] == 1) {
            if (get_random_in_range(10) != 9) {
                if (get_random_in_range(4) != 3) {
                    System.out.println("cleaning");
                    grid[vacuum_current_position] = 0;
                    number_of_cleaned_dirt++;
                    score = score + 10;
                } else {
                    System.out.println("failed to clean and moving on");
                    move_agent_3();
                }
            } else {

                System.out.println("failed to detect the dirt");
                move_agent_3();

            }
        } else {

            if (get_random_in_range(4) != 3) {
                move_agent_3();
            } else {
                System.out.println("depositing dirt by mistake and moving on");
                grid[vacuum_current_position] = 1;
                number_of_dirt++;
                move_agent_3();
            }

        }
    }

    protected static void move_agent_3() {
        number_of_steps_to_clean++;

        if (vacuum_current_position == 0) {
            System.out.println("going right");
            vacuum_current_position = 1;
        } else if (vacuum_current_position == 1) {

            vacuum_current_position = 2;

//            if (get_random_in_range(2) == 1) {
//                System.out.println("going right randomly");
//                vacuum_current_position = 2;
//            } else {
//                System.out.println("going left randomly");
//                vacuum_current_position = 0;
//            }

        } else if (vacuum_current_position == 2) {
            System.out.println("going down");
            vacuum_current_position = 5;
        } else if (vacuum_current_position == 3) {
            System.out.println("going right");
            vacuum_current_position = 4;
        } else if (vacuum_current_position == 4) {
            System.out.println("going up");
            vacuum_current_position = 1;
        } else if (vacuum_current_position == 5) {
            System.out.println("going down");
            vacuum_current_position = 8;
        } else if (vacuum_current_position == 6) {
            System.out.println("going up");
            vacuum_current_position = 3;
        } else if (vacuum_current_position == 7) {
            System.out.println("going left");
            vacuum_current_position = 6;
        } else if (vacuum_current_position == 8) {
            System.out.println("going left");
            vacuum_current_position = 7;
        }
    }

    protected static void work_agent_4() {

        if (grid[vacuum_current_position] == 1) {
            if (get_random_in_range(10) != 9) {
                if (get_random_in_range(4) != 3) {
                    if (get_random_in_range(2) == 1) {
                        System.out.println("cleaning");
                        grid[vacuum_current_position] = 0;
                        number_of_cleaned_dirt++;
                        score = score + 10;
                    } else {
                        System.out.println("not cleaning and moving on");
                        move_agent_2_4();
                    }
                } else {
                    System.out.println("failed to clean and moving on");
                    move_agent_2_4();
                }
            } else {

                System.out.println("failed to detect the dirt");
                move_agent_2_4();

            }
        } else {

            if (get_random_in_range(4) != 3) {
                move_agent_2_4();
            } else {
                System.out.println("depositing dirt by mistake and moving on");
                grid[vacuum_current_position] = 1;
                number_of_dirt++;
                move_agent_2_4();
            }

        }
    }
}
