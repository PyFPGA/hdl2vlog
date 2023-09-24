library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity counter is
  generic (
    WIDTH : positive := 4
  );
  port (
    clk   : in  std_logic;
    rst   : in  std_logic;
    count : out std_logic_vector(WIDTH-1 downto 0)
  );
end entity counter;

architecture RTL of counter is
  signal count_reg : unsigned(WIDTH-1 downto 0) := (others => '0');
begin

  counter_proc: process(clk, rst) begin
    if rst = '1' then
      count_reg <= (others => '0');
    elsif rising_edge(clk) then
      count_reg <= count_reg + 1;
    end if;
  end process counter_proc;

  count <= std_logic_vector(count_reg);

end architecture RTL;
