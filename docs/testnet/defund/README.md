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
peers="7a3c4079964eaca46f63f9a4ba37997ae55bee60@45.85.249.93:27656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,b625169f52cb2b0f020478fd2e6d4b74778b7c1f@109.123.241.104:27656,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,59a9547d142660795cc8cff437a5b780025a8577@109.123.243.33:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
