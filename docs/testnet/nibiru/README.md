# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



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

**live-peers** (28)
```bash
peers="a3cdb006b290cd2e694b451e8e141ee397a24eac@85.190.246.96:26656,bf6a9b21fcf5e1aa02a07348959633d58cf1b307@109.123.246.116:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,8cca1055bd1eb274af9e122119b52be34774f169@95.217.208.233:26656,8371f0340545c708d68572caf6adc4084fe6ba0c@89.117.63.116:26656,c36bcb5907e0ac74018bf42982b249be090e92c1@192.248.150.77:26656,bae5efe7460f77784c0691290616659001c0c012@38.242.205.48:26656,46c0cb4d56ebfd4c69911c59b3f17cb17bcc3ed7@64.226.94.147:26656,ed66095b43d923ecdc73eb77d6193084036888bc@65.108.2.35:26656,75533faca91c0f8b249d268fa888f498feee0ba3@103.253.147.190:26656,e104fb31e9aa612dd36554616eeb2a08e2439e24@80.85.142.176:26656,6caeb82a187923cba406d09d7b8aa08b5552aac1@184.174.36.166:26656,8279e11d79bb4d5ee3595893a546123423e48b6a@109.123.246.138:26656,41a86600b386e2caff1d6912c91be72ec4f1126e@185.202.223.161:26656,c8bb9b0d660d006f097bf5af4b21b2046dbe1ba3@93.183.208.65:26656,141dccaf3cbe958b9409bee5805f2be35da377e5@183.2.149.136:26656,104a00413d0fc7ec208c810c50d49932da355bd5@129.226.159.141:26656,c794911b61dd57c1f3f0517122560c6be90e1da7@89.116.24.183:39656,be2ebed3286033450a2d7a8a15b5f5d4774663d9@89.116.29.69:26656,7d3867934f0664832f782e3579e30686b069c473@109.123.250.109:26656,2ba6745852fcceb6914111a254ad5380ba721848@5.199.133.114:39656,c03ac8a54e2fe73ac59d621eb0262456eca4d3d8@83.169.217.43:39656,7e5a42fb0ff06ff712c7eafb2dccc04caede5f01@38.242.231.237:26656,03b4f35d5956ae641da3fd21d2b84c7fe146c3ed@95.31.241.194:26656,d478d4a34de532833ec1c4df65f3b79f77265f17@35.229.110.80:26656,90e1f35289a3e527e04b59a53c1baeb4d02bdb63@65.108.94.198:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
