# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


## Public endpoints

* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (13)
```
peers="79888e0547bfb9937e4a6f4fbdca7ccbf46cbbde@155.133.23.88:26656,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,3666c65e99775b8149396fd5c781dec6a29fb13b@75.119.144.48:31656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,f296bfda3c0c3f46059c89d3ee02f3f11d95d00b@162.55.234.70:55056,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,8340a33a3794dfef56159f412012c16ce51d96dc@65.109.85.52:46656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,b9e0210809b9dfc9cd299c6e83116d7fa45c6e27@65.109.68.93:46656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.uptickd/config/config.toml
```
