# Supplement recommendations based on fitness goals

def get_supplement_recommendations(goal):
    
    base_essential = [
        {
            'name': 'Whey Protein',
            'icon': '🥛',
            'description': 'Fast-absorbing protein to support muscle repair and growth after workouts.',
            'dosage': '25-30g per serving',
            'timing': 'Post-workout',
            'benefit': 'Muscle recovery',
            'organic': False
        },
        {
            'name': 'Vitamin D3 + K2',
            'icon': '☀️',
            'description': 'Essential for hormone production, bone health and immune function.',
            'dosage': '2000-4000 IU daily',
            'timing': 'With breakfast',
            'benefit': 'Hormonal health',
            'organic': False
        },
        {
            'name': 'Omega-3 Fish Oil',
            'icon': '🐟',
            'description': 'Reduces inflammation, supports joint health and improves recovery time.',
            'dosage': '2-3g EPA+DHA daily',
            'timing': 'With meals',
            'benefit': 'Anti-inflammatory',
            'organic': False
        }
    ]

    if goal == 'gain_muscle':
        essential = base_essential + [
            {
                'name': 'Creatine Monohydrate',
                'icon': '⚡',
                'description': 'Most researched supplement for strength and muscle gains. Increases ATP production.',
                'dosage': '5g daily',
                'timing': 'Any time of day',
                'benefit': 'Strength & power',
                'organic': False
            }
        ]
        recommended = [
            {
                'name': 'Pre-Workout (Caffeine)',
                'icon': '🔥',
                'description': 'Boosts energy, focus and endurance during training sessions.',
                'dosage': '150-200mg caffeine',
                'timing': '30 min pre-workout',
                'benefit': 'Energy & focus',
                'organic': False
            },
            {
                'name': 'ZMA (Zinc, Magnesium, B6)',
                'icon': '😴',
                'description': 'Improves sleep quality and natural testosterone levels for better recovery.',
                'dosage': '1 serving',
                'timing': 'Before bed',
                'benefit': 'Sleep & recovery',
                'organic': False
            },
            {
                'name': 'Beta-Alanine',
                'icon': '💪',
                'description': 'Reduces muscle fatigue and increases endurance during high-intensity training.',
                'dosage': '3.2g daily',
                'timing': 'Pre-workout',
                'benefit': 'Endurance',
                'organic': False
            }
        ]
        optional = [
            {
                'name': 'Ashwagandha',
                'icon': '🌿',
                'description': 'Adaptogenic herb that reduces cortisol, improves strength and boosts testosterone naturally.',
                'dosage': '300-600mg daily',
                'timing': 'With dinner',
                'benefit': 'Stress & strength',
                'organic': True
            },
            {
                'name': 'Maca Root',
                'icon': '🌱',
                'description': 'Natural energy booster that supports hormonal balance and endurance.',
                'dosage': '1500-3000mg daily',
                'timing': 'Morning',
                'benefit': 'Energy & hormones',
                'organic': True
            },
            {
                'name': 'Beetroot Powder',
                'icon': '🫀',
                'description': 'Natural nitric oxide booster that improves blood flow and workout performance.',
                'dosage': '500mg daily',
                'timing': '30 min pre-workout',
                'benefit': 'Blood flow',
                'organic': True
            }
        ]

    elif goal == 'lose_weight':
        essential = base_essential
        recommended = [
            {
                'name': 'Green Tea Extract (EGCG)',
                'icon': '🍵',
                'description': 'Natural fat burner that boosts metabolism and enhances fat oxidation.',
                'dosage': '400-500mg EGCG',
                'timing': 'Before cardio',
                'benefit': 'Fat burning',
                'organic': True
            },
            {
                'name': 'L-Carnitine',
                'icon': '🔥',
                'description': 'Helps transport fatty acids into cells to be burned as energy.',
                'dosage': '1-2g daily',
                'timing': 'Before workout',
                'benefit': 'Fat metabolism',
                'organic': False
            },
            {
                'name': 'Fiber Supplement (Psyllium)',
                'icon': '🌾',
                'description': 'Increases satiety, reduces hunger and supports gut health.',
                'dosage': '5-10g daily',
                'timing': 'Before meals',
                'benefit': 'Appetite control',
                'organic': True
            }
        ]
        optional = [
            {
                'name': 'Garcinia Cambogia',
                'icon': '🌿',
                'description': 'Natural appetite suppressant that may help reduce calorie intake.',
                'dosage': '500mg 3x daily',
                'timing': 'Before meals',
                'benefit': 'Appetite control',
                'organic': True
            },
            {
                'name': 'Apple Cider Vinegar',
                'icon': '🍎',
                'description': 'Improves insulin sensitivity and helps control blood sugar spikes.',
                'dosage': '1-2 tbsp in water',
                'timing': 'Before meals',
                'benefit': 'Blood sugar',
                'organic': True
            },
            {
                'name': 'Cayenne Pepper Extract',
                'icon': '🌶️',
                'description': 'Natural thermogenic that slightly increases metabolic rate.',
                'dosage': '500mg daily',
                'timing': 'With meals',
                'benefit': 'Metabolism boost',
                'organic': True
            }
        ]

    else:  # get_fit
        essential = base_essential
        recommended = [
            {
                'name': 'Multivitamin',
                'icon': '💊',
                'description': 'Covers nutritional gaps and supports overall health and energy levels.',
                'dosage': '1 serving daily',
                'timing': 'With breakfast',
                'benefit': 'Overall health',
                'organic': False
            },
            {
                'name': 'Magnesium Glycinate',
                'icon': '😴',
                'description': 'Improves sleep quality, reduces muscle cramps and supports recovery.',
                'dosage': '200-400mg',
                'timing': 'Before bed',
                'benefit': 'Sleep & recovery',
                'organic': False
            },
            {
                'name': 'Collagen Peptides',
                'icon': '🦴',
                'description': 'Supports joint health, connective tissue and skin elasticity.',
                'dosage': '10-15g daily',
                'timing': 'Post-workout',
                'benefit': 'Joint health',
                'organic': False
            }
        ]
        optional = [
            {
                'name': 'Turmeric + Black Pepper',
                'icon': '🌿',
                'description': 'Powerful anti-inflammatory that reduces muscle soreness and joint pain.',
                'dosage': '500-1000mg curcumin',
                'timing': 'With meals',
                'benefit': 'Anti-inflammatory',
                'organic': True
            },
            {
                'name': 'Ginger Extract',
                'icon': '🫚',
                'description': 'Reduces muscle soreness and inflammation naturally after workouts.',
                'dosage': '1-2g daily',
                'timing': 'Post-workout',
                'benefit': 'Recovery',
                'organic': True
            },
            {
                'name': 'Probiotics',
                'icon': '🦠',
                'description': 'Supports gut health, nutrient absorption and immune system function.',
                'dosage': '10-20 billion CFU',
                'timing': 'With breakfast',
                'benefit': 'Gut health',
                'organic': True
            }
        ]

    return {
        'essential': essential,
        'recommended': recommended,
        'optional': optional
    }