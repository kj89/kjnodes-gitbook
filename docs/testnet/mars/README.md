# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: ON

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Chain explorer
[https://explorer.kjnodes.com/mars-testnet](https://explorer.kjnodes.com/mars-testnet)

## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: [https://mars-testnet.grpc.kjnodes.com](https://mars-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@mars-testnet.rpc.kjnodes.com:45656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@mars-testnet.rpc.kjnodes.com:45659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/mars-testnet/addrbook.json > $HOME/.mars/config/addrbook.json
```

**live-peers** (10)
```bash
peers="c5a39b97f56d73185ceb904899c65ad8d1390364@199.175.98.135:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,1eb8f66ad73bfaad455fa3c9711029a723367642@65.108.67.152:45656,84f1325b17d2d0b7ed78c2f746c2bb515af37d48@65.109.204.197:26656,b36f90fb7763876c5a5999fa3e993f6ef8063969@144.91.66.143:28656,a446002f40b926db596deb7bae9ed3fe04af1c2e@65.108.206.215:17656,79b82583f2d8a0ed187fa2edf1f06c0c712d4989@185.48.24.106:28656,bb2151bd2ffa6f5c93b6cad3d55aaee675a03ef4@161.97.79.100:56656,eb163c2d89d2bfcc1a76a03961c16ea64ad5b58b@157.245.57.33:26656,2bdb587f6202165f3c66b730e437afe00c8de171@194.163.132.91:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
