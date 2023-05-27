# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:14090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:14056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:14059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (9)
```bash
peers="7fd7a5acce9bcafef89b946b4416699f9fd32592@38.242.226.77:27656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,5a173cbd537b8f75063b2db51131fa906236376e@65.109.93.152:32656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,6bb46db441cf84b5941717290a74ee8d853f0bdc@38.242.229.49:27656,ae95d629c68b76c7a0f7695b2e63e6c5464ec435@212.90.120.12:27656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
