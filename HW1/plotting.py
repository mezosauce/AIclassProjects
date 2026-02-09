import pandas as pd
import matplotlib.pyplot as plt
import os

def create_plots():
    if not os.path.exists('results.csv'):
        print("Error: results.csv not found. Please run main.py first.")
        return

    df = pd.read_csv('results.csv')
    
    # List of metrics to plot
    metrics = [
        ('nodes_expanded', 'Nodes Expanded', 'nodes_expanded.png'),
        ('cost', 'Path Cost (Distance)', 'path_cost.png'),
        ('time_ms', 'Execution Time (ms)', 'execution_time.png')
    ]
    
    # Get unique algorithms and test cases for consistent coloring/ordering
    algorithms = df['algorithm'].unique()
    test_cases = df['test_case'].unique()
    
    for column, title, filename in metrics:
        # Pivot the data for easier plotting with pandas
        # index=test_case, columns=algorithm, values=metric
        pivot_df = df.pivot(index='test_case', columns='algorithm', values=column)
        
        # Reorder test cases to match original if needed
        pivot_df = pivot_df.reindex(test_cases)
        
        ax = pivot_df.plot(kind='bar', figsize=(12, 7), width=0.8)
        
        plt.title(f'Comparison of Algorithms: {title}', fontsize=14)
        plt.ylabel(title, fontsize=12)
        plt.xlabel('Test Case', fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(title='Algorithm', bbox_to_anchor=(1.05, 1), loc='upper left')
        
        plt.tight_layout()
        save_path = os.path.join('plots', filename)
        plt.savefig(save_path)
        print(f"Saved plot: {save_path}")
        plt.close()

if __name__ == "__main__":
    create_plots()