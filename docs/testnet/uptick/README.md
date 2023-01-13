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

**live-peers** (16)
```bash
peers="1c66685cbf5c8dc0a739eb57c896d35eb2eed17c@141.94.139.233:28656,2763c95b0c9b0b31c312b06d6ae6887968fb9830@194.163.154.224:26656,94b63fddfc78230f51aeb7ac34b9fb86bd042a77@94.23.207.45:30556,70c19420bb2d40c5a6c3466c69ead6e0877b9cc7@45.85.250.108:26656,eb5a3112a64944e2bd701ff8aa99ab95209c6310@185.198.27.110:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:15656,d8777278648d8fc93800692a8b96a7f104df4f9a@194.163.135.127:26656,883d6557bef1bae68c4fb569078caf0cf4c45bdd@142.132.202.50:26651,962d620d21ce5caba3e765501dd9b309cfac234f@78.31.64.11:26356,821cec653e1bdcd6e0ea7db62ddc65e7dae9fc5b@190.2.136.58:26656,af5262526a0800a29a0a7194e1488a9fa62d0005@195.3.223.208:26656,3cffe20d473b0bd4451d330da8b741b5d42dcb44@65.21.131.215:26666,f06b6a57001440bf3507ba2f09a3010f6d50080b@135.181.133.37:29656,2298edffe9306e4d9370233c1d29dab567829095@144.91.78.28:26656,d6aad702ecfed6c5e76e2f25dea6b921c3cd7857@154.12.242.252:31656,b14b4e3a46180eccf00d816aed5338db925e2237@185.225.191.149:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.uptickd/config/config.toml
```
