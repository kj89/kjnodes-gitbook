# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/lava.png" width="150" alt=""><figcaption></figcaption></figure>

Lava powers a trustless market for RPC data access. The protocol  governs over peer to peer and private Provider-Application pairings,  ensuring high quality RPC service while creating consensus around data served.

**Chain ID**: lava-testnet-1 | **Latest Version Tag**: v0.4.4 | **Wasm**: OFF

[Website](https://lavanet.xyz) | [Discord](https://discord.com/invite/Tbk5NxTCdA) | [Twitter](https://twitter.com/lavanetxyz)




## Chain explorer
[https://explorer.kjnodes.com/lava-testnet](https://explorer.kjnodes.com/lava-testnet)

## Public endpoints

* api: [https://lava-testnet.api.kjnodes.com](https://lava-testnet.api.kjnodes.com)
* rpc: [https://lava-testnet.rpc.kjnodes.com](https://lava-testnet.rpc.kjnodes.com)
* grpc: [https://lava-testnet.grpc.kjnodes.com](https://lava-testnet.grpc.kjnodes.com)

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

**live-peers** (26)
```bash
peers="520d066ec1f72ced0a764f70514bb7de7cf762c0@213.239.216.252:40656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,0325a40dfa74c462cc51e64f1c5e331dff1cae2c@65.109.111.159:38656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,3173b2d34ce415ee9a1bf08646d85688bf49e299@5.189.186.222:36656,cc5b61248a30c7e34ff4a7dfee3d470000b0de2d@194.50.0.178:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,ef6e9620807e7e4614fd8e02722f8075ec277544@199.175.98.122:26656,67ba50d49201090cb09c4d03be2c8db50be2f437@95.217.167.118:26656,38093a87129f828125be65e8969bb7ede682b26c@38.242.197.134:26656,20c13bd0d972acba5588493fb528b558a0317013@38.242.133.203:26656,f9190a58670c07f8202abfd9b5b14187b18d755b@144.76.97.251:27656,18432dbb1238c416053bcbbc7b85b5f1258010a0@193.34.212.34:11134,0735c5a841fe98ee0a74de7cef537c03b4c66a1b@45.89.54.153:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,441fffc1478d480934d11d397384682ac42acd2f@95.217.9.227:26656,6d7ead316f354a549fe22f5ebe72d68ec0af685a@194.233.68.136:44656,e6703109f87389aea6b1ca9b8335a6eddbce50d6@185.182.186.85:26656,0a94c7f8451841f51bfaf86668edd212f181735f@95.214.55.155:21656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,d60e577b6dbdac7a7cd620f71a6bff71f9f82c2e@146.19.24.242:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
