from collections import deque


def create_fireworks(effects, power):
    palm_fireworks = 0
    willow_fireworks = 0
    crossete_fireworks = 0
    while effects and power:
        current_effect = effects[0]
        current_power = power[-1]
        if current_effect >= 0 and current_power >= 0:
            current_firework = current_power + current_effect
        else:
            if current_power <= 0:
                power.pop()
            else:
                effects.pop()
            continue

        if current_effect <= 0 and current_power <= 0:
            effects.popleft()
            explosive_power.pop()

        if current_effect <= 0:
            effects.pop()
            continue
        elif current_power <= 0:
            power.pop()
            continue

        if current_firework % 3 == 0 and current_firework % 5 == 0:
            crossete_fireworks += 1
            effects.popleft()
            power.pop()
        elif current_firework % 3 == 0:
            palm_fireworks += 1
            effects.popleft()
            power.pop()
        elif current_firework % 5 == 0:
            willow_fireworks += 1
            effects.popleft()
            power.pop()
        else:
            effects[0] -= 1
            effects.append(effects.popleft())

        if palm_fireworks >= 3 and willow_fireworks >= 3 and crossete_fireworks >= 3:
            break

    return palm_fireworks, willow_fireworks, crossete_fireworks


def print_result(palm, willow, crossete, effects, power):
    if palm >= 3 and willow >= 3 and crossete >= 3:
        print("Congrats! You made the perfect firework show!")
    else:
        print("Sorry. You can’t make the perfect firework show.")
        if effects:
            print(f"Firework Effects left: {', '.join([str(el) for el in effects])}")
        if power:
            print(f"Explosive Power left: {', '.join([str(el) for el in power])}")
    print(f"Palm Fireworks: {palm}")
    print(f"Willow Fireworks: {willow}")
    print(f"Crossette Fireworks: {crossete}")


fireworks_effects = deque([int(s) for s in input().split(", ")])
explosive_power = [int(s) for s in input().split(", ")]
palm_fireworks, willow_fireworks, crossete_fireworks = create_fireworks(fireworks_effects, explosive_power)
print_result(palm_fireworks, willow_fireworks, crossete_fireworks, fireworks_effects, explosive_power)
