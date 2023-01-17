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

**live-peers** (22)
```bash
peers="5f72f1d09de54a65860bc12e5ab5eac21fd766e3@5.75.202.157:40656,c675bd639c81562cb52e2b14bae0cbaaf78150bf@84.46.249.51:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,f01079014db8293225f708e44725f64a25495145@65.21.187.135:26656,f8093378e2e5e8fc313f9285e96e70a11e4b58d5@141.94.73.39:45656,c1d2c7a810c386595e59ead21ba69555a37ac007@5.161.110.128:26656,5a3e8478405460c847354dc3ab84437b51b2e50b@93.185.166.71:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,8675cc6e69c2043a8dc0a854e769c1f135b5f272@23.88.73.158:26656,9389cefdaa999eb81b93f4354d1077553ceb7a86@217.76.55.76:26656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,4d3b57b07c9b28b6e41757b37b485b8482ed98d9@45.147.199.193:26656,0ab2ceb8999da66cd9eeaa6d7f0e3144c1f7a31e@89.108.109.116:26656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,0176c2127c25f0ecd8383577cd373e0928d20884@86.48.3.14:26656,3e3dfe25eed3a5fb654887902e051a637b8d650a@185.188.249.246:40656,3d57a684fb53f41fb755af5c64d62433b80b1bbd@167.235.206.216:26656,e6b3dc37e08c1807cc044eb56061cfe0186af569@65.108.206.45:27656,20045ce5bdc8fbc356d82351305fe2f9f188a4b5@217.76.55.68:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,409d5422d6934b0dedfd3347e078b67aac691120@45.147.199.185:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
