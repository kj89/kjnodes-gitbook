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

**live-peers** (19)
```bash
peers="20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,4eb0bef7997b87086c40766193d812479238187c@217.76.55.66:26656,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,58d46050cf77065d27e9526a7e93c8f814cc036a@194.146.13.185:26656,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,571d81a83ec9b23f953120b51440cf160d1c04e9@176.124.223.78:26656,5ac71c9178d2f28b67c6c54e1b7871065aefe8da@161.97.81.155:26656,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,c0637ffa6e3a9a92c88820a8320ee58fb807706f@142.132.253.112:40656,9f4ea4b9da9801ba5e97924d13c7c793d94bfec9@45.147.199.176:26656,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,b042f97047a92686b13d300fbddf36eb52542fff@149.154.66.229:26656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,4f865b04ff70dd314c840bb3c324f41edbb3c3ff@164.68.102.102:26656,d8436ce4d85fac4fd245d782966bfcda312b1d54@162.55.1.2:33656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
