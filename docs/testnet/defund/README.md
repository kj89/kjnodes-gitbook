# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" alt=""><figcaption></figcaption></figure>

DeFund is an L1 blockchain built for building decentralized permissionless,  on-chain trading strategies that are packaged into a dETF (decentralized  exchange-traded fund) token, tradable within any ecosystem or CEX.

**Chain ID**: orbit-alpha-1 | **Latest Version Tag**: v0.2.6 | **Wasm**: ON

[Website](https://www.defund.app) | [Discord](https://discord.gg/FV26pRPZ3P) | [Twitter](https://twitter.com/defund_finance)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/defund-testnet](https://explorer.kjnodes.com/defund-testnet)

## Public endpoints

* api: [https://defund-testnet.api.kjnodes.com](https://defund-testnet.api.kjnodes.com)
* rpc: [https://defund-testnet.rpc.kjnodes.com](https://defund-testnet.rpc.kjnodes.com)
* grpc: defund-testnet.grpc.kjnodes.com:40090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:40656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:40659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (29)
```bash
peers="424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,c2974fd847a286f1b960f5a7a63b96f582c88f48@207.244.227.247:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,cf28e64a237c7278223238325727cef0c2c8ca51@193.34.217.174:26656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,86caf6297ae00fb58b58a272984275c592b2fdf7@65.109.84.216:56656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,e04063d21e8e4ef2ca3661c6b20a5192c1afe119@138.201.204.5:32656,4515f69283a8f3db159d35e72edce0ea0ddb6f1b@38.242.142.134:28656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,578a034282182f8ce129eedd4ef1b074ca4d3032@16.163.74.176:26616,d7b1896a0dad8f7c5d77cb8656271c972120ce55@154.53.54.154:30656,0f2506a8c83b9cbeb08685829db26a4f7a0db6b0@65.21.5.11:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,8105e993c0d6af1da517691267c236009e478bf1@144.76.225.172:13656,15f51735fd76f72abfca70f4bb2da93458b63073@93.100.235.162:26656,8abfa09fdbea667157d96f79c815fd9b3186b6ae@65.109.92.240:2026,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
