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

**live-peers** (36)
```bash
peers="36909ce5289d8f994fb2562f7a188a79ce826359@141.95.145.41:27656,a3cac2328bb41f44c17c437ff8ee29d46b91ae0c@38.242.139.95:26656,d04084623a4ec44fd91d46f07ba2e2d1d0638dd4@141.95.23.183:26656,0544670a43be0a61c7e354bc55d32b6573dc31cf@94.131.106.79:26656,b2521331cc7ef94374208aae2c1ed8a3dcdd811b@95.217.118.100:28656,219c417bd9de04c60f730abd4769e981f10c083b@109.123.249.191:26656,e6b3dc37e08c1807cc044eb56061cfe0186af569@65.108.206.45:27656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,20151f8b15d6f3ad670f5bfc1c747de72e96fb3f@194.180.176.128:26656,2a138efb5ef0638386af44c3df32ccdc8895b4d0@65.21.172.60:36656,58437bc62307a512f391db5c1e24e3cff8b9f8d3@136.243.88.91:2070,5ac71c9178d2f28b67c6c54e1b7871065aefe8da@161.97.81.155:26656,7ca31e50d5509104ea481869bcbe91e6883fe9d0@135.181.150.198:36656,1a01a583c1a0ffedbf3623236fe0eeb15489cc62@51.81.57.80:10356,e4470dac98f2cee5bd060c52c7d801d57bfc9308@185.245.182.206:26656,d9d5f9a4ca3cb5ab7db0e6735b0ce8c246eceb6b@135.181.214.190:26656,d31d9801e7a021d287570b94ffcf27b91b0d9b66@217.76.55.74:26656,a488bdf909f71f64c7948f1cb783bd29af66f3ae@23.88.66.239:33656,ccace1585ce7d671f09d4d442d77936b29ee8118@164.68.127.182:26656,a28ed6c0af36097350181d5fa2d116f6e93585fe@38.242.139.91:26656,7831e762e13c2cb99236b59f5513bf1f8d16d036@88.99.3.158:10356,b5f48558fd70799ae123bd879ce12205478be379@135.125.180.36:20756,f6a16b8fd8e43442d9cbe852fa6104dc743c3383@38.242.139.242:26656,95d487c4f51295c4cd799cc7fe53d23ea7298bdf@206.246.71.251:46656,d325bc4677b9a10d9acc2f34982f8001099e7e2b@88.210.6.152:26656,bee3cc2feaafa0eb98f5044d9f0ac11f7b8d468e@185.225.191.23:26656,4f865b04ff70dd314c840bb3c324f41edbb3c3ff@164.68.102.102:26656,0484eab6881ba458c5988296403963aaf273700b@157.90.236.25:18656,e199e4d17120559bc34357d72f6595cbcd4d5cd4@173.212.216.232:26656,57eadf177e7429db82bfdbed6fa0521e8741e404@94.130.13.40:26656,c734239cb2a4a59e69de4fc52a9c4aca57285391@199.175.98.107:26656,09ce2d3fc0fdc9d1e879888e7d72ae0fefef6e3d@65.108.105.48:11256,c34b4bc09946950d3fb8059d4954f45ed24e25bc@89.163.255.100:26656,a78c5a1fa7b12eef729fa3dec3b7c3b073552664@45.147.199.191:26656,b2d88a66cd3da5bcfcee01ad3baa892d51bfca42@15.235.10.157:26656,67742399a48abc97c7eef61b1a60b96c720122c2@45.147.199.180:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
