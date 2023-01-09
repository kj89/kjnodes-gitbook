# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.0 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)


## Public endpoints

* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@lava-testnet.rpc.kjnodes.com:44656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@lava-testnet.rpc.kjnodes.com:44659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/lava-testnet/addrbook.json > $HOME/.lava/config/addrbook.json
```

**live-peers** (17)
```bash
peers="cab9892dd329b0308af3b8364356757f874d17fe@65.109.87.135:13656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,470ab82dd419e1652267d8b4c5acaa4522e78145@45.14.194.30:26656,0c7f5b6515e2fef06ad9f4771ac1d77ac62b2df1@146.19.24.142:29656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,1ec38451f3e45535ceba905d1442310c69aaf93e@217.76.61.37:26656,f7c1a998b8ef7cae7e38b0eff64d96206924e957@45.84.138.167:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,72aabf4950afe5f2514cff8dc6c2c56600e7ed03@34.251.254.15:26656,4975932e4eba3d4e8fd0eb6668ab21268602f3c5@147.182.237.170:38656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,3a79f4b1aa71a330a9ff302da692fbeefbfc1247@95.217.9.227:26656,fe1998168f5336811a79fbcaf2d5d5a69f2f9f63@65.108.81.145:26656,1bc84553189d26f993f730ca901b69ee6118bc36@161.97.132.107:26656,d3eb474a1f90d004e49638e384069c32d7dcc8a2@185.252.232.110:26656,0a78dd75926983ba06de451480673487ffa1bcc1@199.175.98.106:26656,5464a7a1982d527844ee93a9d9c24e478c4e09ed@34.29.69.27:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
