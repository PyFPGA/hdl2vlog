module counter #(
  parameter WIDTH = 4
) (
  input                    clk,
  input                    rst,
  output logic [WIDTH-1:0] count
);

  always_ff @(posedge clk or posedge rst) begin
    if (rst) begin
      count <= '0;
    end else begin
      count <= count + 1;
    end
  end

endmodule
