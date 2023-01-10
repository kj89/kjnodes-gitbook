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

**live-peers** (10)
```bash
peers="28f14b89d10992cff60cbe98d4cd1cf84b1d2c60@88.99.214.188:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,09ce2d3fc0fdc9d1e879888e7d72ae0fefef6e3d@65.108.105.48:11256,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,9cbaf117258ac247bce37f314d1a2ddba34b5ad6@194.163.190.54:26656,5ac71c9178d2f28b67c6c54e1b7871065aefe8da@161.97.81.155:26656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,a3cac2328bb41f44c17c437ff8ee29d46b91ae0c@38.242.139.95:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
