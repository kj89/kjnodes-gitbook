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
peers="391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,f093208f6cd6bea470cef7cc9dba1d4e12fd8284@38.242.153.85:26656,ad41ef68f4740d5be84ff54c34b0331b02ff4ae4@85.10.193.246:29656,6c37c542748d1d78c3c0d96eb7c5f1af5ee6a770@213.202.211.70:26656,3a0b54203d91571398a5b4538a938fd464c4d871@176.117.185.56:40656,daeabf9286ea1331f07f7981c5425aeca5db1f5b@95.217.5.233:26656,d88eb958f18940d75add40b51d2a69295ed9e378@5.75.245.162:26656,93b0696cd10a3d683c1cf28641ff210d316954da@89.117.63.232:26656,2ce838eea29c3f6ca650081dd0fa99186304b151@37.99.82.28:26656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,96f253c371a7f7f854faf7ffc5e0ee9fc4f8dd7f@165.227.32.93:26656,d55b0afead31b23179fb6c2e6e514eb4b3199672@5.104.108.100:39656,f4a8fb180fbbb4c44e7721368cbc6ce3f9fc47e1@5.189.140.55:26656,b9f203a7d45a2a2766ff144ea9cc680987886772@85.239.242.186:26656,3edbefe333daf987dea52dd53e776add12483e70@193.203.15.44:26656,f31536c1f70fb1a8127c1f412bbccef4d1a19e20@195.14.6.2:26656,1da145d81ca9d5d9ccd55f529435056a27fcdeef@184.174.34.227:26656,fd5d54740618e8ca6d85cae52ec2db5ea8ac8ea5@91.107.196.77:26656,f6c4429af0c199f579d55b3b12b760e431db21d4@34.139.52.143:26656,a2162bd42fdb011eb821d62fcaed3276142cf4d4@162.55.80.116:27656,4b38d4082e88f3623233915c240f112b25b442ba@84.46.245.66:26656,bf6a9b21fcf5e1aa02a07348959633d58cf1b307@109.123.246.116:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,f863c87c1562e1d42065ee0f61e4daef9e51aa69@84.46.251.4:26656,549a5eb615e8560105f3801315a07c49c1804f48@158.220.98.245:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,6b69faf2cd1287de0c12e04aefcde72b6578ce40@82.208.21.249:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
