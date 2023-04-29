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
peers="5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,01eb6fc83d3ef9757696c2f72ab7cc3c2cd393e7@193.34.217.183:26656,b44266dc79cf178ca2bc690bcae949efffe77ae7@51.15.0.91:26656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,15f51735fd76f72abfca70f4bb2da93458b63073@93.100.235.162:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,ca8488007cb12caf5fd76dec032157a07999d45b@91.226.253.197:30756,a79130668102f116a23cfcf9fd94623de4a223fe@81.30.157.35:10656,617229160b712399ebb39e0880167c5e83873d73@167.172.138.167:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,ad644354fe8141fd01250f186fe2abd11453c6d7@185.209.223.44:40656,cdadad3c8fc2982484fe7fd4fd041dcd437c6f8e@116.202.225.84:13656,7c459f88962a4d07d7ccd6d0c94f891bb7a7ada0@65.109.26.21:13656,8abfa09fdbea667157d96f79c815fd9b3186b6ae@65.109.92.240:2026,a73bd40070102d04a89de86e7b3fe1c7fbcc394d@89.163.209.3:40656,d0c6f2febf03bbf69a3cd1c5fb489d7febfc34b9@65.109.116.119:40656,fa3b9aa4309d5e473040e71bca3fbd93f85bb842@65.108.110.23:40656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,c2974fd847a286f1b960f5a7a63b96f582c88f48@207.244.227.247:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
