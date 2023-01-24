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

**live-peers** (25)
```bash
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@185.16.39.172:27066,2e727665d138eb0d526163514f21ddb57299a5b5@80.92.206.180:26656,c83d7b205b2e80bd9a33c13161bd39d520988455@38.242.139.189:26656,8a089094624f27698f365402a059b8b810532805@207.180.229.129:26656,e61d0d5eb484e778d842da903cc49dd74a802a57@5.180.151.155:26656,c5c98017339ce6d4d5d2a4fd0fb1aaeb966ef0f7@65.108.124.57:36656,474e2436e097c28472a1fe269e1825762fa340d6@38.242.128.19:26656,97a7c2941a5875ce518f4775b841ff3b888c82d4@65.108.129.104:21656,5464a7a1982d527844ee93a9d9c24e478c4e09ed@35.232.127.103:26656,632bfd3276ab33ed74cbb048a1de28183b927e9c@80.85.141.179:26656,acc3fe0b067e10b55c060b2f740d6193bf15a315@15.204.207.179:26656,d5ad7ae6caf54ef20a6dc04d30a55caac6c540c9@5.61.41.138:26656,9225ba24c2c0562d139306c945d2d00f9e55bf9c@185.219.142.88:26656,cd1324c315249f690e2582d7ed4ff63d2aa9158e@86.48.31.236:26656,00a146a28a56967cb8fc65933c69b051f7327d1a@86.48.31.241:26656,4e84acb55f6a222b31e92b0a00738ee8c46c0770@86.48.31.235:26656,fb498cc17f301930cfd4d3b6e6261148c84e05e7@45.140.147.117:27656,e54aa82a12a05480488042e46e9f433bd4238df1@185.219.142.75:26656,ab9d16be78cf75437418991fff62d65ec1101e43@5.180.151.165:26656,167ea5dfb340d4b78acd48d435b880cdd23b9019@45.159.189.14:26656,821c9347c927db52138dcd4bb54478fdf17f273e@81.0.218.53:26656,33298ebaaa99faad4f5c9880f555340f26ff66ff@161.97.160.19:26656,ade4d8bc8cbe014af6ebdf3cb7b1e9ad36f412c0@176.9.82.221:19956,3c47fd1662bcb17a4713c23e41d7b25e34478b8e@103.19.25.157:26672,3a445bfdbe2d0c8ee82461633aa3af31bc2b4dc0@3.252.219.158:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.lava/config/config.toml
```
