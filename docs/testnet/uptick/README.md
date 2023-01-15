# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/uptick.png" width="150" alt=""><figcaption></figcaption></figure>

The Business Grade Multi-Chain NFT Infrastructure for Web 3.0

**Chain ID**: uptick_7000-2 | **Latest Version Tag**: v0.2.4 | **Wasm**: OFF

[Website](https://uptick.network) | [Discord](https://discord.gg/UzeHS7fu5H) | [Twitter](https://twitter.com/uptickproject)


## Public endpoints

* api: [https://uptick-testnet.api.kjnodes.com](https://uptick-testnet.api.kjnodes.com)
* rpc: [https://uptick-testnet.rpc.kjnodes.com](https://uptick-testnet.rpc.kjnodes.com)
* grpc: [https://uptick-testnet.grpc.kjnodes.com](https://uptick-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@uptick-testnet.rpc.kjnodes.com:15656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@uptick-testnet.rpc.kjnodes.com:15659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/uptick-testnet/addrbook.json > $HOME/.uptickd/config/addrbook.json
```

**live-peers** (9)
```bash
peers="883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,3cffe20d473b0bd4451d330da8b741b5d42dcb44@65.21.131.215:26666,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,7a4f1c0baa2ff31c02163fb658c4eb8d119193c7@95.214.52.173:26656,b483acbcae7ccd1244f588144245e9d1124c3de5@88.99.56.200:26666,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
