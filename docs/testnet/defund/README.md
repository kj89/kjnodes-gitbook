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

**live-peers** (28)
```bash
peers="2425a645f1b375c4d61857a7010841d4baf74a1b@109.195.131.79:36656,424b76ff5aadcc5a58debf8e02ca251c2e521050@168.119.165.240:26456,ad644354fe8141fd01250f186fe2abd11453c6d7@185.209.223.44:40656,2151e36f7696b39147f995c5171805c4eae0788a@194.87.113.40:26656,bccd2003a7eb23008479c76427ac2c276160e09a@75.119.154.72:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,beb10b655c17c4dd306c5afe51b5bcb81ff46e9c@195.128.158.119:26656,5a93bbc7e9dc368ccadd2627b35364e0bf06035e@31.187.74.29:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,48920dc679562d2f116f0b89ac77796377cfb130@194.146.13.254:26656,fb124c136c3aa20a71c68d9cb0a2833293c8dc58@23.88.73.158:26656,51c8bb36bfd184bdd5a8ee67431a0298218de946@162.19.237.229:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,bc934501cffc27940d96e7775b6b8ae5122604ab@185.185.80.195:28656,a461ba3b41468076d1a45a547dd5d9f74b017527@3.16.186.56:26656,8274cf9149b23c23694cdce7045a607879fc51b2@95.217.182.26:26456,4b740c782cc4e6561de519fffb23499f0541e84d@89.116.29.202:18656,8185e22360e3d43bd7cb8dc41f402f367285c49e@65.21.3.95:40656,8105e993c0d6af1da517691267c236009e478bf1@144.76.225.172:13656,1a4f0f016ffc8f6814835dc20f5bb7050b2eac90@38.242.239.25:26656,8abfa09fdbea667157d96f79c815fd9b3186b6ae@65.109.92.240:2026,ca8488007cb12caf5fd76dec032157a07999d45b@91.226.253.197:30756,6b9797483562f7836e0ab23e63b911daf324b55d@65.108.238.147:28656,8af843d901c5b2e5ad35c4b89b8888432384a56c@95.165.107.241:40656,ecc08f67284282b930d2c200772d2b2d29d5bbcd@5.9.122.49:13656,e1b25355c160820148744c91d7ec79fea69b18bf@185.144.99.73:26656,617229160b712399ebb39e0880167c5e83873d73@167.172.138.167:26656,9446504166663fc0090b81abdf86fafe93e72a40@185.209.30.95:40656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
