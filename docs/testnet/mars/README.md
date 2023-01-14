# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: OFF

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


## Public endpoints

* api: [https://mars-testnet.api.kjnodes.com](https://mars-testnet.api.kjnodes.com)
* rpc: [https://mars-testnet.rpc.kjnodes.com](https://mars-testnet.rpc.kjnodes.com)
* grpc: https://mars-testnet.grpc.kjnodes.com:443

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
peers="3bf10fbfc288a40498631e6ccfa6fe806dc78656@162.55.245.219:17656,2bdb587f6202165f3c66b730e437afe00c8de171@194.163.132.91:26656,934c311b462b889c2e9899fcd42e3523896d2548@65.108.97.58:2866,cdbc11052bdc3c126df2ea84bfbb8175e2f2f0e8@95.217.85.254:15603,846ee4df536ddba9739d3f5eebd0139b0a9e5169@159.148.146.132:27225,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,c50858f3d8f48b394d9a859b117bf7e7a5470185@91.107.243.215:26656,ceac7c696d16e9cac1f3988e7578b1d651e245c5@85.10.202.135:33656,e12bc490096d1b5f4026980f05a118c82e81df2a@85.17.6.142:26656,5adc56a96c2d7925d454075c110edca3c79bdd33@65.109.69.240:43656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
