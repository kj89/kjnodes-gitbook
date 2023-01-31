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

**live-peers** (29)
```bash
peers="24a2bb2d06343b0f74ed0a6dc1d409ce0d996451@188.40.98.169:27656,14ae45e7f2ff7491cfa686a8fcac7cc095bc38ff@213.239.217.52:39656,b1223ecc0fdde9d72551b9223f69b5310f870a67@85.208.51.197:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:44656,8f79bf6093fd728359f529a4a5214c0364749230@65.21.205.248:11656,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,6a55747d1f93e46696f233ac563e28fea24afc47@38.242.237.192:36656,e593c7a9ca61f5616119d6beb5bd8ef5dd28d62d@34.246.190.1:26656,eb7832932626c1c636d16e0beb49e0e4498fbd5e@65.108.231.124:20656,5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,a20e24a251c9e6325a7c1e05d6a479bcd9c721ac@168.119.52.60:26656,3a750868d3284cc4a07be4a878333e38b44b94bf@144.91.111.1:26656,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656,d9703df8c0e5eef6c0766217d611a13ed6ee8d95@88.99.33.248:26656,34271a6f82d755777a3db02be39e575bf4ebd415@65.109.30.197:28656,6f71395e15c9f9f439df51fc6a667d93a1b7b019@35.162.117.131:26656,5b25ec3860445e50a41a80850970b3241350df72@194.233.90.134:26656,8a20f8f798c5073f0867812e691f54b5cd0dd65d@109.123.242.188:26656,ef6e9620807e7e4614fd8e02722f8075ec277544@199.175.98.122:26656,a5c1d2e86c2dc0eecb009dc71c92d6b5e193db6b@35.210.166.150:26656,433be6210ad6350bebebad68ec50d3e0d90cb305@217.13.223.167:60856,550d7467d6a442da11d9772b804252a8dfdca27e@91.107.243.149:26656,149f9f017344ce9cebb637baa7cab57a28f3a8c3@86.111.48.159:26656,420704479ed1e13f862ee08162e40325107fef14@115.74.127.184:26656,0c548b2704594c7929b713de4c6985b9d9f03b8a@194.163.184.46:27656,39309f1ce3d7b6acf9714c749b67c7db6d3f615d@38.242.152.174:26656,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,5676c8606f23471e220f8bf7317498a61bb93194@65.21.134.202:26686,4634ca7cefe997035440df1095915ed255e81296@49.12.189.98:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
