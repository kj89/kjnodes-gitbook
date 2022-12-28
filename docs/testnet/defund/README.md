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

**live-peers** (11)
```
peers="58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,c94423f1f435b7e12d05c2d59ed3a0373833d3c3@157.90.253.129:26656,8ee475f4b4574176f4e9d5d111dba6724e0ad62b@37.120.163.114:26656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,6854d36513081c77a24987ab66a436e29e3e5cfa@65.21.131.215:26576,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,0d190196414307625a087a2d3cd02756fb4643a7@65.108.13.185:26767,ca14da988f14920eb15bb99f289c10527aacdc35@185.244.180.226:26656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
