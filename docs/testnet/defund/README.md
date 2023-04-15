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

**live-peers** (28)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:40656,773b4e59036c6934cdd3c919fc74259aba7d8ab3@185.16.39.4:26656,f417252166d6508a75371573f3c12e8abca238a5@65.108.108.52:13656,34b72721aa503574a0709b1859fb1da2aa12ce70@88.99.3.158:11256,d1c8bfe892396220d19c8815dcc4e536aaf0e080@164.68.127.58:26656,1a8e8d6667615f4836c1c1403563a26a1044fd00@116.203.158.189:26656,09ad8591e50abf7954cf15d50558f375128a17f4@168.119.118.183:26656,da77231e4a499106b2fa2f0d64e553c2a9e2203b@65.108.199.206:28656,0ac70993664bc792bd7e5f2384eb520bec7a4b76@95.165.107.241:26656,230d474bebd608fa076c7ae2585a180fdc1befae@185.252.233.99:26656,ffb2898494cdbd6625d962ea4511c29507177c62@164.68.103.176:26656,26975c5bb7dc42463cc6361ea3c75f325e801917@85.10.197.4:40656,205f6826808509bb8be87bfff953dd422bfff962@207.180.254.16:28656,04ff1f98174b35960d8bc2d10bf0da1406f7028b@194.146.12.215:27656,ba0abf77c2dec230a7ae06b32d1abf63dbd48642@5.9.82.120:60656,fc8ad183d32ca52eabc2d3af8e1e85b06ca1286a@159.89.117.7:26656,bc3d614b684c8e1647f4196dc8a785b1ab0381ef@65.108.13.154:33656,020abb71537ac87559814e1cb85cbd837046e836@23.88.5.169:23656,23c52b4aa95a5b269277292410f6f4c8815e616c@194.163.174.103:27656,af0aee9f4b50d9ea30b64be0ab78415824ab87c7@65.21.237.241:26656,0a03781fa64c2f2810cbbaacb81418170f53fe13@45.88.188.253:26656,65b7c9a6fa81e532e701e9179b890b3038a86962@149.102.136.186:27656,13b2cd52bb5d82993ca872b9152ec7d70a811714@136.243.136.241:21656,035ff6d94b5c62d1830d71b25c259e11a679250d@38.242.158.116:27656,e26fda3a5a7ff3177cb49a98890f8132ea34c442@212.33.229.66:26656,22fa766ffe457fd1236ea88bce1f40bf4bbaf328@77.91.100.131:26656,c659b2e0ec4027e6d4977c49917bdbd27451203f@130.185.119.129:26656,2ea2700b0082d8d5bc9ed2f13b36af47cc787ea7@80.254.8.54:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.defund/config/config.toml
```
