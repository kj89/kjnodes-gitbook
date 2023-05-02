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
* grpc: defund-testnet.grpc.kjnodes.com:14090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@defund-testnet.rpc.kjnodes.com:14056
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@defund-testnet.rpc.kjnodes.com:14059
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/defund-testnet/addrbook.json > $HOME/.defund/config/addrbook.json
```

**live-peers** (30)
```bash
peers="6406dc6dff130a009ad79bb04eb29b731414811f@141.95.145.41:27656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,cee0d215e82cadb63f7067c8d0d7848cb24f034d@65.109.25.58:13656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,354485ffcd96d2c292969fae86624f754924bb8c@91.77.165.172:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@146.59.47.207:26836,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656,9c9d6b57948fae5cf1c690f3b339ad1200ce0dd2@91.201.112.91:40656,5a62ea143c84ac41b06296672e2d0ba1c9d0da1c@178.20.40.143:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,05379608ba4640178a1357199ac9cbc7c5ba686c@37.78.130.124:39656,8dd9f0759495b4e05ebd68a6c1600824cbed9044@65.109.48.181:28656,11c0952beaf78a6452d270c7bd344c25406e1b16@95.217.212.66:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,a079b21b69e5c2a53087128701e904d2b0ed0ff8@5.199.133.109:26656,79d5c2746cf510a66606ab1d9600545b311425a8@38.242.143.63:28656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,0f49d79093241c410062423ddbeda83cccbbc16d@154.53.62.243:40656,ffc319ea701f7769f96fb746a01ef204b1222815@178.18.255.221:26656,0537a8d627b65f65c810206dffef9fa820183167@65.109.160.32:40656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,ed9d651a48968b4c3c8e8f01e15dbb451eed195a@5.75.138.108:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
