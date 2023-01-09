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

**live-peers** (20)
```bash
peers="254da4ac248771ded96df539f7f70abbae5c3d93@161.97.77.186:26656,b2521331cc7ef94374208aae2c1ed8a3dcdd811b@95.217.118.100:28656,2c17ee3ba85f8c5690d8a95c59927e87a3fce14b@195.201.197.4:40656,5ac71c9178d2f28b67c6c54e1b7871065aefe8da@161.97.81.155:26656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,85518a1363fc284c2a315f0ca937ebf855783d60@65.108.238.217:11144,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,09ce2d3fc0fdc9d1e879888e7d72ae0fefef6e3d@65.108.105.48:11256,0544670a43be0a61c7e354bc55d32b6573dc31cf@94.131.106.79:26656,d1976601f04df2a2c7e35c0e8212464acfb7512e@75.119.147.235:26656,f6a16b8fd8e43442d9cbe852fa6104dc743c3383@38.242.139.242:26656,331bd82dc918ffaaf75284ae54b35bbb94f8e216@144.126.138.249:30656,4c291b33574d679e43f7cec340ba4befecec0724@161.97.152.115:26656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,f5c51a2c40257da4524776717f91590ccad593ec@176.124.221.134:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,f0e1b5cbade7abe4a23fb12d0359c5bc40213718@95.217.109.222:26656,cb503107b4135363d5ff83ff6a1a1423d8db4166@62.171.169.230:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
