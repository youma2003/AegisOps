// aegis-probe (M1): simulates the server fleet, publishes metrics, injects chaos.
// For now it only exposes /healthz on :2112. gRPC ProbeService (:50051) comes next.
package main

import (
	"log/slog"
	"net/http"
	"os"
)

func main() {
	logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))

	mux := http.NewServeMux()
	mux.HandleFunc("/healthz", func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("ok"))
	})

	logger.Info("aegis-probe starting", "http", ":2112")
	if err := http.ListenAndServe(":2112", mux); err != nil {
		logger.Error("http server stopped", "err", err)
		os.Exit(1)
	}
}
