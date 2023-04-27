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

**live-peers** (27)
```bash
peers="ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,427cfff6caf2d3f294e1adef874b17a9047b9a0c@194.163.185.141:26656,736c0d6962c283e49ac4b4c1d2df4e9335d9923c@38.242.145.186:26656,668ae8cb141c97d3fc27930bda216d94459e2790@135.181.253.203:26656,25e01aa86dae35ef0207991d1da02b7a9adf5e4a@38.242.219.103:26656,345cfe2a2081fee1788ee54fbb106be4900c0294@148.251.10.110:27060,cf755b5d8b1c400dd003221e461d717a8535c007@83.167.103.221:26656,aa999ecb4e74d0b95465638670cd6fddc9c1f544@65.109.89.37:26656,cf13f41c223c6e47e581f6ae8ec7c554218de8fc@207.244.251.201:26656,62ceb0aaa166dbe32c4870e5333f7bed0c7bb288@173.249.54.158:26656,ce3b4ebe9c6890c73b28faf854a759d54c3ffaa3@38.242.128.233:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,24b9df9d8b731fe559a749a76d7466c6646c2d23@65.21.200.124:26656,31fa18ff28fd7f80d279a951849e4ef56003b039@128.140.85.113:26656,dd80caf5a8080ef255a181e06f89d5fcf0dac15c@65.108.232.182:11656,0f8ea9f1dacc680e7074e8019bae16b1e8979977@89.117.58.243:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,8eff5b8e877d4f48f6363468840d0265c18d500a@167.172.181.179:39656,1e886c522cd043092062bec284e3f87a3e310b2f@45.8.133.159:26656,639bf251f6fe8b1d11c322c40a44e1c0f6ebf3e7@82.208.23.171:26656,40f831a2b8a28e32e2ac6b62f2cf3621d3de6e54@185.217.126.168:26656,8152c22a9f4b0587426291b077c018a3ad5361b8@38.242.195.246:26656,b380fa4928c0a8078b5046f6f70991395aa3f79e@91.107.232.208:26656,072113660767e89b71033ce214f8248d2fb88862@194.163.167.126:26656,de5eef4a640ca1c05e0f4b5102ace1e531c88478@38.242.154.181:26656,dc3e07aedd921389dffacf8deb4aa257fef7da90@178.128.206.147:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
