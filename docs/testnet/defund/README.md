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
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:60656,0108df8793ec07fa82ea202d54b70c603b827ea4@5.9.81.251:60656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,9d93136c7e4af2de3f8bb6c82c5d1f0b30b7b657@38.242.225.217:27656,195f80fa7d564efd62304bcb7da85f0a50f3d7db@109.123.254.113:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
