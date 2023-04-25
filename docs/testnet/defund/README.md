# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/defund.png" width="150" alt=""><figcaption></figcaption></figure>

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
peers="251c53c762273adbb7853569d17af2a6f00e9c7a@65.108.101.124:13656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,a73bd40070102d04a89de86e7b3fe1c7fbcc394d@89.163.209.3:40656,13b2cd52bb5d82993ca872b9152ec7d70a811714@136.243.136.241:21656,dd82f0b844645b2047fa1b5a54f7fe575e80a134@188.34.167.232:26656,afdbe2fb845ff591d32f83e4a28b49c59cd9111c@65.109.117.121:13656,2674582e77f339ac5bcb9c048f9b1457df27fc57@65.108.150.197:40656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,2931b7010fbbef00c06fd200e26989d903c1a249@89.163.155.252:27656,183059b7a637f856a500d5062a809a29de2812fc@161.97.78.40:26656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,4be5080f72bb03ecd6453f427b80d9f211fad9e3@194.146.13.187:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,4739d4708a7ca86c086a1af6a1ff432e6f5947b8@38.242.239.193:29656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,e3c348467a8c88c0f65e2ca8a71875d2a384b8b4@185.16.39.19:60656,18921a27facf3760d59147e4ae176b1bdf226346@195.201.237.172:18656,083d01165dd48373b212b25a7d7a811655ce1074@95.111.243.155:26656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,9c9d6b57948fae5cf1c690f3b339ad1200ce0dd2@91.201.112.91:40656,fee92379b94d5bd81c7af58b6161bce2f10870fe@158.220.104.193:26656,91bbf1434b741862e406ab87c014fdff3cc96109@77.232.40.71:26656,d8652a72fa5b61ad82fea2ca3be8b710b56ba88a@38.242.199.69:26656,fb95f32da1b85cb4c1fa04c2e75b045352a5507f@5.104.108.71:26656,26bdbcbfa286f443c842ed241d35fa09065d586b@161.97.128.243:34656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
