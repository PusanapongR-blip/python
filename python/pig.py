import random
import sys

# กำหนดค่าคงที่
MAX_SCORE = 30
MIN_PLAYERS = 2
MAX_PLAYERS = 4

def roll():
    """ทำการทอยลูกเต๋า (O(1))"""
    return random.randint(1, 6)

while True:
    players_input = input(f"Enter number of players ({MIN_PLAYERS}-{MAX_PLAYERS}) or 'q' to quit: ").lower()
    if players_input == 'q':
        print("Goodbye! May be next time.")
        sys.exit() # ออกจากโปรแกรมทันที
    if players_input.isdigit():
        players = int(players_input)
        if MIN_PLAYERS <= players <= MAX_PLAYERS:
            break
        else:
            print(f"Please enter a number between {MIN_PLAYERS} and {MAX_PLAYERS}.")
    else:
        print("Invalid input. Please enter a number or 'q'.")

player_scores = [0] * players
    
print("-" * 30)
print(f"Game starts! Target score: {MAX_SCORE} points.")
print("-" * 30)
    
game_over = False

# ลูปหลักของเกม: ทำงานจนกว่าจะมีผู้ชนะ
while not game_over: 
    # ลูปวนรอบผู้เล่นทุกคน
    for i in range(players):
        # ตรวจสอบผู้ชนะก่อนเริ่มรอบผู้เล่นคนถัดไป
        if max(player_scores) >= MAX_SCORE:
            game_over = True
            break
                
        player_index = i + 1
        current_turn_score = 0
        is_rolling = True

        print(f"\n--- Player {player_index}'s turn (Current Score: {player_scores[i]}) ---")
            
        # ลูปย่อยสำหรับการทอยลูกเต๋าต่อกันในหนึ่งในรอบเดียว
        while is_rolling and not game_over:
            rolling = input(f"Press 'r' to roll, 'p' to pass (Turn Score: {current_turn_score}): ").lower()
                
            if rolling == 'p':
                # ผู้เล่นผ่าน: เพิ่มคะแนนรอบนี้เข้าร่วมคะแนนรวม
                player_scores[i] += current_turn_score
                print(f"Player {player_index} passed. New total score: {player_scores[i]}")
                is_rolling = False
            elif rolling == 'r':
                roll_result = roll()
                print(f"Roll: {roll_result}")
                
                if roll_result == 1:
                    # ได้ 1: เสียคะแนนรวมทั้งหมด
                    player_scores[i] = 0
                    print("💀 You rolled a 1! Score reset to 0.")
                    is_rolling = False
                else:
                    current_turn_score += roll_result
                        
                    # ตรวจสอบผู้ชนะทันทีที่คะแนนรวมถึง
                    if player_scores[i] + current_turn_score >= MAX_SCORE:
                        player_scores[i] += current_turn_score
                        game_over = True
                        is_rolling = False
                    else:
                        print(f"Turn score: {current_turn_score}")

# แสดงผลลัพธ์สุดท้ายเมื่อเกมจบ
print("\n" + "=" * 30)
print("✨ GAME OVER - FINAL SCORES ✨")
winning_score = max(player_scores)
for i in range(players):
    status = " (WINNER!)" if player_scores[i] == winning_score and player_scores[i] >= MAX_SCORE else ""
    print(f"Player {i + 1}: {player_scores[i]} points{status}")