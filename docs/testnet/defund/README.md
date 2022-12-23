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
peers="c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,72ab81b6ba22876fc7f868b58efecb05ffac9753@65.109.86.236:28656,bad21eb0dd7d2002912acc42a89b66a0deb44a03@65.21.134.202:26576,27184beff22d064a593233bbe6b0883f9f7fc2ff@45.87.104.74:26656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,b914bb37cc8d1b7fb91579a79f7438a24d16de65@45.147.199.172:26656,7df51b9f8ec9405fddb7c35b534a70fe70f6b93e@194.163.191.80:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.defund/config/config.toml
```
