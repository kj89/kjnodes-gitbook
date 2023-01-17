# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-4 | **Latest Version Tag**: v0.2.2 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: [https://defund-testnet.grpc.kjnodes.com](https://defund-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (13)
```bash
peers="11dd3e4614218bf584b6134148e2f8afae607d93@142.132.231.118:26656,8368bb579d1c98230a65f9b46d495b003353a784@65.108.206.118:36656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,d9f1a0f399c8db62206edb2be29a313829fc8521@135.181.128.19:26656,5e7853ec4f74dba1d3ae721ff9f50926107efc38@65.108.6.45:60556,a70bd4fe605503061d823689e3f3abe3b6397975@45.147.199.189:26656,e104f008f6d1227170d3b4ce1d73f0ea2068094f@84.201.162.168:26656,b6849dcff65d91bc9376366d788cd958a6e0f5df@45.147.199.174:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,0ab2ceb8999da66cd9eeaa6d7f0e3144c1f7a31e@89.108.109.116:26656,20045ce5bdc8fbc356d82351305fe2f9f188a4b5@217.76.55.68:26656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
