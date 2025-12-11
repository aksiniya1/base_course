def mechanical_energy(mass, height, velocity, g=9.81):

    potential_energy = mass * g * height
    kinetic_energy = (mass * velocity ** 2) / 2
    total_energy = potential_energy + kinetic_energy
    
    return total_energy

energy1 = mechanical_energy(mass=2, height=10, velocity=5)
print(f"Масса: 2 кг, Высота: 10 м, Скорость: 5 м/с")
print(f"Полная механическая энергия: {energy1:.2f} Дж")

