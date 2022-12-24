# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: defund-private-3 | **Latest Version Tag**: v0.2.1 | **Wasm**: OFF

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)


## Public endpoints

* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (10)
```
peers="748e7c000dc2fe6ac66686884f8533fc7916b6a3@38.242.244.163:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,8ee475f4b4574176f4e9d5d111dba6724e0ad62b@37.120.163.114:26656,36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,2c17ee3ba85f8c5690d8a95c59927e87a3fce14b@195.201.197.4:40656,c0098c96773cbd0d7507d037768845c582f1a878@65.108.202.230:27656,2093ca0548db1553f55ad5a983ce154d04ed5ea4@146.19.24.52:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,7725b464de9314636d0e0124d046d4b63606ff09@5.161.99.35:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
