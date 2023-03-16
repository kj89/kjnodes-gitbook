# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/bitcanna.png" width="150" alt=""><figcaption></figcaption></figure>

BitCanna is a proof-of-stake (POS) decentralized payment network designed exclusively to serve the cannabis industry. 

**Chain ID**: bitcanna-dev-1 | **Latest Version Tag**: v1.6.2 | **Wasm**: OFF

[Website](https://www.bitcanna.io) | [Discord](https://discord.gg/9AVrzaVQvs) | [Twitter](https://twitter.com/BitCannaGlobal)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/bitcanna-testnet](https://explorer.kjnodes.com/bitcanna-testnet)

## Public endpoints

* api: [https://bitcanna-testnet.api.kjnodes.com](https://bitcanna-testnet.api.kjnodes.com)
* rpc: [https://bitcanna-testnet.rpc.kjnodes.com](https://bitcanna-testnet.rpc.kjnodes.com)
* grpc: bitcanna-testnet.grpc.kjnodes.com:42090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@bitcanna-testnet.rpc.kjnodes.com:42656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@bitcanna-testnet.rpc.kjnodes.com:42659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/bitcanna-testnet/addrbook.json > $HOME/.bcna/config/addrbook.json
```

**live-peers** (6)
```bash
peers="80ee9ed689bfb329cf21b94aa12978e073226db4@212.227.151.143:26656,e72441f66d5101289c9fd86f6733c43551b1d04d@89.58.59.75:46656,2175709bdd102641e9e4ddd38ba263b7f06214df@65.109.28.177:26356,0a18b1d8d1bbd8abc07da8fa0902dbbd33cbd2ef@65.109.10.161:26050,60fae2c5581622bb84eaf95878e85c9f339f1a2a@212.227.151.106:26656,b0c7e5c69aaf00626baaf7c59370029b587a91a4@65.109.92.240:30006"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.bcna/config/config.toml
```