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
peers="2c17ee3ba85f8c5690d8a95c59927e87a3fce14b@195.201.197.4:40656,d34cf8cb422c13d19f7ba20614d33eac24e0f9fc@116.202.241.157:35656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,5db1142851dd1c7106779aa9d348a9f67a630df0@164.68.110.234:26656,e26b814071e94d27aa5b23a8548d69c45221fe28@135.181.16.252:26656,9e67baeac323278617e9036a892464b21dfe3a38@65.108.71.92:45656,4d3b782ab389525370f53d40e970b1362bc92106@185.182.186.202:26656,2a87e54d6849058523a0d761318cb1258c4299df@77.91.123.14:26656,b1c64cdd7bd0f798eaa0239fd0cee26e770628b3@194.233.82.172:29656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
