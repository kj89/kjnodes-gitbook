# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/mars.png" width="150" alt=""><figcaption></figcaption></figure>

Mars is a credit protocol for the future: non-custodial,  open-source, transparent, algorithmic and community-governed.

**Chain ID**: ares-1 | **Latest Version Tag**: v1.0.0-rc7 | **Wasm**: OFF

[Website](https://marsprotocol.io) | [Discord](https://discord.gg/marsprotocol) | [Twitter](https://twitter.com/mars_protocol)


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
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:45656,c50858f3d8f48b394d9a859b117bf7e7a5470185@91.107.243.215:26656,e12bc490096d1b5f4026980f05a118c82e81df2a@85.17.6.142:26656,7342199e80976b052d8506cc5a56d1f9a1cbb486@65.21.89.54:26653,c4ea4f6f288d5704a8675c833a8f2dc640498620@135.181.59.182:28656,846ee4df536ddba9739d3f5eebd0139b0a9e5169@159.148.146.132:27225,76226517bd06932c9e0957bd4dd7b995227cdaa4@95.216.242.177:33656,c84154bb4aba1cd78169ac2b30d34ee8a1966c6e@194.163.179.175:16656,2bdb587f6202165f3c66b730e437afe00c8de171@194.163.132.91:26656,3bf10fbfc288a40498631e6ccfa6fe806dc78656@162.55.245.219:17656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.mars/config/config.toml
```
