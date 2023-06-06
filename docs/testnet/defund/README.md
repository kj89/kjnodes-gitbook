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
peers="1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,7ea4373346eea6b2c4f77655883e915481609028@185.177.116.123:27656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,6b9797483562f7836e0ab23e63b911daf324b55d@65.108.238.147:28656,4f1d96f5b8adb5bcdd59e61cb6e387ff12422a41@65.109.63.110:13656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:14056,7fd7a5acce9bcafef89b946b4416699f9fd32592@38.242.226.77:27656,ccebeed4dae0fe100826f7c7c111d4d62c4bb546@109.123.240.111:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
