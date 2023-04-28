# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibirufi) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (29)
```bash
peers="b380fa4928c0a8078b5046f6f70991395aa3f79e@91.107.232.208:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,8072df736e7fcaf23aae3252f05677cd693cae03@38.242.249.207:26656,afb1e9da1d33badfaf8c11098a4b4571d3ac7f05@31.220.86.26:39656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,5c052c78ab48d0b26098574ba8b04e039209769a@95.217.1.96:26656,1532fb485391af0fb7b06cc089f6d71dad196c77@31.220.94.106:39656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,359ab5a45015c75b0ca847519254cb8d0aa3aa6c@65.108.206.74:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,96285853644bd5c35db33b033abfed598c9c10c0@75.119.130.70:26656,b6fe0cb29a6cca2acd41aade05c46272db5c7c0c@209.126.83.209:26656,492adb0eac00feacaeef1aaa9496b8cdb513de44@45.14.194.188:26656,5db2f2c82ba2b9c431d069270ebc16d35985ffaa@91.230.110.96:26656,4432207b04118601f777ac93a5c3dd441b968734@70.34.250.4:26656,30f177d9b55510559bf1467f81e0ea18310781b6@178.163.77.190:27656,d0b30b6fdd2df3e70e41fb0ba43b400e7d02e6e0@38.242.252.252:26656,668f3f60a0ff3f9fcbaf8551782f71de1cc767a9@89.116.24.215:26656,9174c2c90723a515a6303513abf6444eb13aba8c@45.85.249.107:26656,ef3361ee215ecc52ac9cb0e25b16d6dd8b899fd0@154.53.51.114:29656,bd4e84bd7b14201661c958c6cb6a1de2a27078ed@95.217.156.62:26656,a10fd4adadd7ca8f430ad88ffdc93366e9471b00@149.102.135.51:26656,f4fa2e13e64628d96f9158a6a2afbb19ebac574e@85.190.246.120:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,d00cdd120096a5464984f29ec360f720677da2fe@89.116.24.30:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
